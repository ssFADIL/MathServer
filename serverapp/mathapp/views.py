from django.shortcuts import render

def gst_amt_calc(request):
    gst_amt = None
    if request.method == 'POST':
        try:
            price = float(request.POST.get('price'))
            gst = float(request.POST.get('gst'))
           
            if price >= 0 and gst >= 0:
                gst_amt = price + ((price * gst) / 100)
            else:
                gst_amt = "Error: Inputs cannot be negative."
        except ValueError:
            gst_amt = "Error: Invalid input. Please enter numeric values."
    context = {
        'gst_amt': gst_amt
    }
    return render(request, 'mathapp/math.html', context)