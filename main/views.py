from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import threading
import os

from main.forms import ReviewForm
from main.process import predict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a = os.path.join(BASE_DIR, 'main')
model_path = os.path.join(a, 'model.h5')


class HomeView(TemplateView):
	template_name = 'home.html'

	def get(self, request):
		print(model_path)
		form = ReviewForm()
		
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		print(model_path)
		form = ReviewForm(request.POST)
		print(form.is_valid())
		print(form.errors.as_data())
		#print(form.non_field_errors())
		if form.is_valid():
			review = form.cleaned_data['review']
			res = predict(review)
			if res < 0.5:
				return redirect('negative')
			else:
				return redirect('positive')

		return render(request, self.template_name)


class PosView(TemplateView):
	template_name = 'pos.html'


class NegView(TemplateView):
	template_name = 'neg.html'
