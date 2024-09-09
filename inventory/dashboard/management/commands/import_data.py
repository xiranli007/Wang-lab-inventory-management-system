import pandas as pd
from django.core.management.base import BaseCommand
from dashboard.models import Culture

class Command(BaseCommand):
    help='Import data from CSV or Excel file into the database'

    def add_arguments(self, parser):
        # add a positional argument naamed 'file_path' in str type
        parser.add_argument('file_path', type=str, help='The file path to the CSV or Excel file')
    
    # define the logic when the command run
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path'] # retrieve the file_path variable from the kwargs library
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file_path)
        else:
            self.stdout.write(self.style.ERROR('Unsupported file format')) # throw an error is other file type is given
            return # exist the command
        
        for index, row in df.iterrows():
            object, created = Culture.objects.get_or_create(
                organism = row['Organism'],
                boxNumber = row['Box_number'],
                copySaved = row['Copy_saved'],
                idNumber = row['id_number'],
                description = row['Description'],
                isolationSource = row['Isolation_source'],
                alternateDesignation = row['Alternate_designation'],
                receivedFrom =row['Received_from'],
                ReceivedDate = row['Received_date'],
                originallyReceivedFrom = row['Originally_received_from'],
                additionalInfo = row['Additional_info'],
            )
            if created:
                object.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully imported row {index}'))
            else:
                self.stdout.write(self.style.WARNING(f'Row {index} already exists'))
            self.stdout.write(self.style.SUCCESS('Data import completed'))