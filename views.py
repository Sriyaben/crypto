
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import start_scraping_task
from .models import ScrapingTask

class StartScrapingView(APIView):
    def post(self, request):
        coins = request.data.get('coins', [])
        if not coins:
            return Response({"error": "No coins provided"}, status=status.HTTP_400_BAD_REQUEST)
        job_ids = start_scraping_task.delay(coins)
        return Response({"job_id": job_ids}, status=status.HTTP_200_OK)

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        tasks = ScrapingTask.objects.filter(job_id=job_id)
        if not tasks.exists():
            return Response({"error": "Job ID not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"job_id": job_id, "tasks": [task.output for task in tasks]}, status=status.HTTP_200_OK)
