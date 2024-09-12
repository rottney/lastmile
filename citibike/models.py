from django.db import models

# Create your models here.
'''
https://gbfs.lyft.com/gbfs/2.3/bkn/en/system_regions.json
	data
		regions
			n
				region_id
				name
	last_updated
	#ttl
	#version
'''
class SystemRegions(models.Model):
	region_id = models.CharField(primary_key=True, max_length=200)
	name = models.CharField(max_length=200)


'''
https://gbfs.lyft.com/gbfs/2.3/bkn/en/station_information.json
	data
		stations
			n
				station_id
				name
				short_name
				lon
				lat
				#rental_uris
					#ios
					#android
				capacity
				region_id
	last_updated
	#ttl
	#version
'''
class StationInformation(models.Model):
	station_id = models.UUIDField(primary_key=True)
	name = models.CharField(max_length=200)
	short_name = models.CharField(max_length=200)
	latitude = models.FloatField()
	longitude = models.FloatField()
	capacity = models.IntegerField()
	region_id = models.ForeignKey(SystemRegions, on_delete=models.CASCADE, db_column="region_id")


'''
https://gbfs.lyft.com/gbfs/2.3/bkn/en/station_status.json
	data
		stations
			n
				num_bikes_disabled
				#num_scooters_unavailable
				num_docks_disabled
				num_docks_available
				#num_scooters_available
				station_id
				is_renting
				last_reported
				vehicle_types_available
					0
						vehicle_type_id
						count
					1
						vehicle_type_id
						count
				num_ebikes_available
				num_bikes_available
				is_returning
				is_installed
	last_updated
	#ttl
	#version
'''
class StationStatus(models.Model):
	station_id = models.UUIDField(primary_key=True)
	is_installed = models.IntegerField()
	is_renting = models.IntegerField()
	is_returning = models.IntegerField()
	num_bikes_available = models.IntegerField()
	num_bikes_disabled = models.IntegerField()
	num_ebikes_available = models.IntegerField()
	num_docks_available = models.IntegerField()
	num_docks_disabled = models.IntegerField()


# don't think I actually need this
'''
https://gbfs.lyft.com/gbfs/2.3/bkn/en/vehicle_types.json
	data
		vehicle_types
			0
				vehicle_type_id
				form_factor
				propulsion_type
			1
				max_range_meters
				vehicle_type_id
				form_factor
				propulsion_type
	last_updated
	#ttl
	#version
'''
'''
class VehicleTypes(models.Model):
	vehicle_type_id = CharField(primary_key=True)
	max_range_meters = FloatField(blank=True, null=True)
	form_factor = CharField(max_length=200)
	propulsion_type = CharField(max_length=200)
'''


# add this later, maybe
'''
https://gbfs.lyft.com/gbfs/2.3/bkn/en/system_alerts.json
	data
		alerts
	last_updated
	#ttl
	#version
'''
'''
class SystemAlerts(models.Model):
	pass
'''
