from django.shortcuts import render_to_response
from django.contrib.auth import get_user_model
from django.template.context import RequestContext
from django.http import HttpResponse
from django.conf import settings
from twython import Twython
import json
User = get_user_model()
from twython_django_oauth.models import TwitterProfile
from urllib2 import urlopen
from django.http import HttpResponse
from django.http import JsonResponse
#from django.utils import simplejson  



SOCIAL_AUTH_TWITTER_KEY ='NWF2Bfb6NVgf35Sd64mItG9DA'
SOCIAL_AUTH_TWITTER_SECRET = 'Nn1ujnXd9rZkM5XzCHJeBysG22JKKaRlaanD253Kb7LJfHSGE2'
Access_Token	= '65716726-3czqZ3oC8N7wBuCh7txY1LLKgUSqoudoHNxAWRy4C'
Access_Token_Secret	= 'AjWiszzVbqI3xFVGIhXOS2lPtfRqDfQOGi9s6s1Rlvm5T'
def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})  # adding request object to the object
   return render_to_response('dockermon/home.html',
                             context_instance=context)

def search(request):
	# from googlemaps import Client
	# api_key = 'AIzaSyCfC7QUUsgZ9oQhQTE2gE7Qx-l8uj0swlk';
	# gmaps = Client(api_key)
	# address = 'Constitution Ave NW & 10th St NW, Washington, DC'
	# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
	# print geocode_result

	# context = RequestContext(request,
 #                           {'request': request,
 #                            'geo': json.dumps(geocode_result)})  # adding request object to the object	
	
	 return render_to_response('dockermon/search.html'	
	)
def geocode(request):
	from googlemaps import Client
	api_key = 'AIzaSyCfC7QUUsgZ9oQhQTE2gE7Qx-l8uj0swlk';
	gmaps = Client(api_key)
	address = 'Constitution Ave NW & 10th St NW, Washington, DC'
	geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
	print geocode_result

	         
	return HttpResponse(json.dumps(geocode_result))  	
	
def latest_tweet(request):
	twitter = Twython(SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET)

	auth = twitter.get_authentication_tokens(callback_url='http://localhost:8000/')
	tweets =  twitter.search(q='iam', result_type='popular')

	twitter1 = Twython(SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET)

	#tweet = twitter.get_user_timeline(count='10')
	print tweets
	# parsed = json.loads(tweet)
	# print json.dumps(parsed, indent=4, sort_keys=True)
	#user_tweets = twitter1.get_user_timeline(12345)
	#user_tweets = "as"
	# twitter1 = Twython(SOCIAL_AUTH_TWITTER_KEY, access_token=Access_Token)
	# user_tweets = twitter1.request("https://api.twitter.com/1.1/statuses/user_timeline.json", "GET", {'screen_name': 'ivinpolosony'})

	twitter = Twython(SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET, Access_Token, Access_Token_Secret)

	response = twitter.get_user_timeline(count=5)
	user_tweets = response
	#user_tweets = json.dumps(user_tweets, sort_keys=True,
	#		indent=4, separators=(',', ': '))
	for x in user_tweets:
		print json.dumps(x, sort_keys=True,
			indent=4, separators=(',', ': '))





	context = RequestContext(request,
                           {'request': request,
                            'tweets': user_tweets})  # adding
	return HttpResponse(json.dumps(user_tweets))
	
def search_tweet(request):
	twitter = Twython(SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET)

	query = request.GET.get('q')
	# tweet_search_result =  twitter.search(q=query, result_type='popular' , count=10)
	tweet_search_result =  twitter.search(q=query,  count=10)

	# tweet_search_result = json.dumps(tweet_search_result, sort_keys=True,
	# 		indent=4, separators=(',', ': '))
	print "TWEEEEEEEEEEEEEEEEEEEEEET"+str(tweet_search_result['statuses'])
	for x in tweet_search_result:
		print json.dumps(x, sort_keys=True,
			indent=4, separators=(',', ': '))




	context = RequestContext(request,
                           {'request': request,
                            'user': request.user,
                            'tweet_search_result':tweet_search_result

                            })
	return render_to_response('dockermon/search_tweet.html',
                             context_instance=context)


def fb(request):
	context = RequestContext(request,
                           {'request': request,
                            'user': request.user,
                            'api_key':settings.SOCIAL_AUTH_FACEBOOK_KEY

                            })

	return render_to_response('dockermon/fb.html',
                             context_instance=context)


def myloc(request):
	context = RequestContext(request,
                           {'request': request,
                            'user': request.user,
                            'api_key':settings.SOCIAL_AUTH_FACEBOOK_KEY

                            })

	return render_to_response('dockermon/myloc.html',
                             context_instance=context)

def cal(request):
	context = RequestContext(request,
                           {'request': request,
                            'user': request.user,
                            'api_key':settings.SOCIAL_AUTH_FACEBOOK_KEY

                            })

	return render_to_response('dockermon/cal.html',
                             context_instance=context)

def whthr(request):
	url = "http://api.openweathermap.org/data/2.5/forecast?q=London,us&mode=json"
	json = urlopen(url).read()
	print json
	return render_to_response('dockermon/whthr.html')


def main(request):
	return render_to_response('dockermon/main.html')
