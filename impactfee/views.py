from django.shortcuts import render
from django.http import request
from django.views.generic.edit import FormView
from .models import UseSubType, Residential
from .forms import ServiceAreaCalculatorForm
from django.contrib.messages.views import SuccessMessageMixin 


class CalculatorView(SuccessMessageMixin, FormView):
    form_class = ServiceAreaCalculatorForm
    template_name = 'impactfee/home.html'
    success_url = ""

    def get(self, request, *args, **kwargs):
        #form = self.form_class
        form = self.form_class(initial={'service_area': '1', 'use_type': '1'})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ServiceAreaCalculatorForm(data=request.POST)
        

        # Store Form Variables:
        # Only used in Fee Display for Service Area
        areas = form.data['service_area'] 
        if areas == '1':
            area = 'Area A'
        elif areas == '2':
            area = 'Area B'
        elif areas == '3':
            area = 'Area C'

        # Used for Select fields - Use Type, Use Sub Type, Units, and Square Feet
        usetype = form.data['use_type']
        subtype = form.data['use_sub_type']
        units = form.data['units']
        squarefeet = form.data['square_feet']

        # Calculates fee based on provided data calculated with database values
        fees = calculateFees(self.request, usetype, subtype, units, squarefeet)
        # Returns fees for display results, area for display results, 
        # form for Select dropdowns, and usetype for changing squarefeet text in fee results on calc.html 
        context = {'fees': fees, 'area': area, 'form': form, 'usetype': usetype}

        if form.is_valid():
        # Renders Fee Display Page
            return render(self.request, 'impactfee/calc.html', context)

# subtype is used to query database values for correct fees
# usetype is used to determine if residential or non-residential
# units used by Hotel and Residential for fees
# squarefeet is used to multiply by fees
def calculateFees(request, usetype, subtype, units, squarefeet):
    #template_name = 'impactfee/fees.html'
    # Used for fee calculation (fee * /per 1000 feet)
    if squarefeet > '0':
        square = (int(squarefeet) / 1000)

    # Residential Fees Calculated
    if usetype == '1':
        if int(squarefeet) < 751:
            id = 1
        elif int(squarefeet) > 751 and int(squarefeet) < 1251:
            id = 2
        elif int(squarefeet) > 1251 and int(squarefeet) < 1751:
            id = 3
        elif int(squarefeet) > 1751 and int(squarefeet) < 2251:
            id = 4
        elif int(squarefeet) > 2251 and int(squarefeet) < 2751:
            id = 5
        elif int(squarefeet) > 2751 and int(squarefeet) < 3251:
            id = 6
        elif int(squarefeet) > 3251 and int(squarefeet) < 3751:
            id = 7
        else:
            id = 8
        
        res = Residential.objects.get(pk=id)
        # Base Fees Used for Fee Display
        parkfee = int(res.parksandrecfee)
        policefee = int(res.police)
        firefee = int(res.fire)
        streetsfee = int(res.streets)
        # Fees Calculated by Units Refering to residential squarefeet table
        parks = round((parkfee * int(units)), 2)
        police = round((policefee *  int(units)), 2)
        fire = round((firefee *  int(units)), 2)
        streets = round((streetsfee *  int(units)), 2)
        admin = 50
        total = round((parks + police + fire + streets + admin), 2)
        subtype = None
    else: 
        # Non-Residential Fees Calculated
        sub = UseSubType.objects.get(pk=subtype)
        parkfee = int(sub.parksandrecfee)
        policefee = int(sub.police)
        firefee = int(sub.fire)
        streetsfee = int(sub.streets)
        # Hotel subtype == '7' uses unit quantity instead of square feet
        if subtype == '7':
            parks = (parkfee * int(units))
            police = (policefee * int(units))
            fire = (firefee * int(units))
            streets = (streetsfee * int(units))
            admin = 50
            total = (parks + police + fire + streets + admin)
        else:
            parks = round((parkfee * square), 2)
            police = round((policefee * square), 2)
            fire = round((firefee * square), 2)
            streets = round((streetsfee * square), 2)
            admin = 50
            total = (parks + police + fire + streets + admin)

    context = {'parks': parks, 'police': police, 'fire': fire, 'streets': streets, 'admin': admin, 
        'total': total, 'parkfee': parkfee, 'policefee': policefee, 'firefee': firefee, 
        'streetsfee': streetsfee}
    return context

# Used to created dropdown dependencies for use_type and use_sub_type
def load_types(request):
    template_name = 'impactfee/subs.html'
    type_id = request.GET.get('use_type')
    use_sub_types = UseSubType.objects.filter(usetypeid=type_id).order_by('id')
    return render(request, template_name, {'use_sub_types': use_sub_types})

# About Application Page
def contact(request):
    return render(request, 'impactfee/contact.html')

# About Application Page
def about(request):
    return render(request, 'impactfee/about.html')