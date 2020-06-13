# CS530Project

Website Link - lostmybag.ipq.co

Project Code Link - https://gitlab.com/avinashcherukuri/530-iwc-project

This is Bag tracking app which help you to keep you bag organized and in case you loose it, we can track it down.

You can add as many bags as you want. Through CreateTag functionality
Using ViewTag, you can view all you bags with unique Tag ID.
once you create Tag for bag, you can create QR code for same. Which will point to SendText url with TagID
In case you loose it, and someone scans QR code. It will send text to register number. When it sends number, based on visitor of app(client), it IP will be looked up.
Via API based on IP, geo location will be tracked and sent in Text message.

GeoIP API = ipdata
SMS API = twilio
QR API = qr
Bot API = Telegram API