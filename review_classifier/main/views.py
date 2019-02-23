from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import threading

from main.forms import ReviewForm
from main.process import predict

class HomeView(TemplateView):
	template_name = 'home.html'

	def get(self,request):
		form = ReviewForm()
		
		return render(request, self.template_name,{'form':form})


	def post(self,request):
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = form.cleaned_data['review']
			res = predict(review)
			if res <0.5:
				return redirect('negative')
			else:
				return redirect('positive')

		return render(request,self.template_name)

class PosView(TemplateView):
	template_name = 'pos.html'

class NegView(TemplateView):
	template_name = 'neg.html'