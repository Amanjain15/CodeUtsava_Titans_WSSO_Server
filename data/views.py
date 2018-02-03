from django.shortcuts import render
from models import *
from django.http import JsonResponse
from test_data import data_list1, data_list2, element_data
# Create your views here.
from decimal import Decimal
import requests, json, multiprocessing as mp

SUCCESS = {
	"success":True
}


def api_call(url, habitation):
	response = requests.get(url)
	# print response.status_code
	data = json.loads(response.text)
	if data['status'] != 'ZERO_RESULTS':
		location =  data['results'][0]['geometry']['location']
		latitude = location['lat']
		longitude = location['lng']
		habitation.latitude = latitude
		habitation.longitude = longitude
		habitation.save()
		# print habitation, village

def get_location(habitation):
	key = 'AIzaSyCzLoN1PtGXixi9lw9dBk5AKoa1FkfiDlM'
	village = habitation.village
	panchayat = village.panchayat
	block = panchayat.block
	district = block.district

	# address = "%s+%s+%s+%s+%s"%(habitation.name, village.name, panchayat.name, block.name, district.name)
	address = "%s+%s"%(panchayat.name, district.name)

	url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'
	url = url%(address, key)
	p = mp.Process(target = api_call, args = (url, habitation))
	p.start()

def load(data_list):
	keys = ['state', 'district', 'block', 'panchayat', 'village', 'habitation', 'element', 'count']
	statment = "%s='%s'"
	for data in data_list1:
		for key in keys:
			exec(statment%(key, data[key]))

		count = Decimal(count)
		# for key in keys:
		# 	print key, eval(key)

		state, state_created = StateData.objects.get_or_create(name = state)
		district, district_created = DistrictData.objects.get_or_create(state = state, name = district)
		block, block_created = BlockData.objects.get_or_create(district = district, name = block)
		panchayat, panchayat_created = PanchayatData.objects.get_or_create(block = block, name = panchayat)
		village, village_created = VillageData.objects.get_or_create(panchayat = panchayat, name = village)
		habitation, habitation_created = HabitationData.objects.get_or_create(village = village, name = habitation)
		if habitation_created :
			get_location(habitation)
			pass
		element = ElementData.objects.get(name = element)
		HabitationElementData.objects.create(habitation = habitation, element = element, count = count)
	#check and notify


def populate(request):
	for element in element_data:
		ElementData.objects.get_or_create(name = element['name'],
			hazards = element['hazards'],
			remedy = element['remedy'],
			permissible_limit_low = element['permissible_limit_low'],
			permissible_limit_high = element['permissible_limit_high'])
	load(data_list1)
	load(data_list2)

	return JsonResponse(SUCCESS)
