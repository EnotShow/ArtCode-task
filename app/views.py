from django.shortcuts import render, redirect

from .parser import get_api_data


def app_view(request, selected_term=None, selected_brand=None, selected_style=None):
    if request.method == "GET":
        terms = get_api_data('terms')
        brand_terms = get_api_data('brand_terms')
        styles = get_api_data('styles')
        context = {'terms': terms, 'brand_terms': brand_terms, 'styles': styles}
        if selected_term and selected_brand and selected_style:
            context['selected_term'] = selected_term
            context['selected_brand'] = selected_brand
            context['selected_style'] = selected_style
            print(selected_style)
        return render(request, 'app/index.html', context=context)
    elif request.method == "POST":
        data = request.POST
        return redirect(f"/s-{data['terms']}/b-{data['brand_terms']}/st-{data['styles']}")
