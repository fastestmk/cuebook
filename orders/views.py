from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.template.loader import render_to_string
from .serializers import OrderSerializer
import webbrowser
import base64
import tempfile


class OrderInvoiceAPI(APIView):

    def post(self, request):
        print(request.data)

        client_name = request.data.get('client_name')
        client_email = request.data.get('client_email')
        client_address = request.data.get('client_address')
        client_gst = request.data.get('client_gst')
        biller_name = request.data.get('biller_name')
        biller_email = request.data.get('biller_email')
        biller_address = request.data.get('biller_address')
        biller_gst = request.data.get('biller_gst')
        services = request.data.get('services')
        bank_account = request.data.get('bank_account')

        total = 0
        for service in services:
            service["total_cost"] = service["service_cost"]+service["tax"]
            total += service["total_cost"]


        # print(services)
        # return 0    
        context = {
            "client_name": client_name,
            "client_email": client_email,
            "client_address": client_address,
            "client_gst": client_gst,
            "biller_name": biller_name,
            "biller_email": biller_email,
            "biller_address": biller_address,
            "biller_gst": biller_gst,
            "services": services,
            "bank_account" : bank_account,
            "total": total
        }


        invoice_html = render_to_string('invoice_1.html', context=context)    



        fh, path = tempfile.mkstemp(suffix = ".html")
        print("pthhhhhhhhhhhhh", path)
        url = 'file://' + path

        with open(path, 'w') as fp:
            fp.write(invoice_html)
        webbrowser.open(url)   


        return Response(invoice_html)
