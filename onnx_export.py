from waffle_hub.hub.adapter.ultralytics import UltralyticsHub

# hub = UltralyticsHub.load("SafetyNet_v3.0.0")
hub = UltralyticsHub.load("HelmetNet_v2.0.0-m")  # BUG: not working
hub.export()