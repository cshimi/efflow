python manage.py makemigrations
python manage.py migrate

# Start the Django development server
python manage.py runserver

. /Users/christianashimitra/anaconda3/bin/activate && conda activate /Users/christianashimitra/anaconda3/envs/MachineLearningTraining;


# delete database
python manage.py shell
from your_app.models import UploadedFile
UploadedFile.objects.all().delete()
YourModelName.objects.all()
