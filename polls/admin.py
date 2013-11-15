from django.contrib import admin
from polls.models import Poll

class PollAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question']
	fieldsets = [
		(None,	{'fields': ['question']}),
		('Date information', 	{'fields': ['pub_date']}),
	]

admin.site.register(Poll, PollAdmin)