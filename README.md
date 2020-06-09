# CS530Project

Website Link - lostmybag.ipq.co

Project Code Link - https://gitlab.com/avinashcherukuri/530-iwc-project

This is Bag tracking app which help you to keep you bag organized and in case you loose it, we can track it down. 
1. You can add as many bags as you want. Through CreateTag functionality
2. Using ViewTag, you can view all you bags with unique Tag ID.
3. once you create Tag for bag, you can create QR code for same. Which will point to SendText url with TagID
4. In case you loose it, and someone scans QR code. It will send text to register number. When it sends number, based on visitor of app(client), it IP will be looked up.
5. Via API based on IP, geo location will be tracked and sent in Text message.

GeoIP API = ipdata
SMS API = twilio