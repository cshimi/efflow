def find_selected_file(selected_file_name):
    return UploadedFile.objects.filter(file=selected_file_name).first()
    print('find_selected_file')


def upload_new_file(uploaded_file, existing_files):
    print('upload_new_file')
    if uploaded_file.name.endswith('.csv'):
        if uploaded_file.name not in existing_files:
            storage_path = os.path.join('media', 'uploads', uploaded_file.name)
            file_instance = UploadedFile(file=uploaded_file)
            file_instance.save()
            return file_instance
    return None

def process_csv(file_path):
    print('process_csv')
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
            csv_reader = csv.reader(csvfile)
            data = list(csv_reader)

        summary = {}
        for row in data[:5]:
            key, value = row[0].split(';=')
            key = key.strip().replace(':', '')
            summary[key.strip()] = value.strip().strip('"')

        data = data[6:]
        return summary, data
    except FileNotFoundError:
        return None, None

def display_file(request, file_id):
    print('display_file')
    try:
        file_instance = get_object_or_404(UploadedFile, pk=file_id)
        summary, data = process_csv(file_instance.file.path)

        if summary is None or data is None:
            raise Http404("File does not exist")

        return render(request, 'analysis/display_csv.html', {'summary': summary, 'data': data, 'file_instance': file_instance})
    except UploadedFile.DoesNotExist:
        raise Http404("File does not exist")

def upload_file(request):
    print('upload_file')
    existing_files = get_existing_files()
    uploaded_file = request.FILES.get('csv_file', None)
    print(existing_files)
    file_already_exists = False
    file_upload_failed = False

    if request.method == 'POST':
        selected_file_name = request.POST.get('existing_file')

        if selected_file_name:
            selected_file = find_selected_file(selected_file_name)
            if selected_file:
                return redirect('display_file', file_id=selected_file.pk)
            else:
                return render(request, 'analysis/file_not_found.html')
        elif uploaded_file:
            file_instance = upload_new_file(uploaded_file, existing_files)
            if file_instance:
                return redirect('display_file', file_id=file_instance.pk)
            else:
                file_already_exists = uploaded_file.name in existing_files
                file_upload_failed = True

    return render(request, 'analysis/upload.html', {
        'existing_files': existing_files,
        'uploaded_file': uploaded_file,
        'file_already_exists': file_already_exists,
        'file_upload_failed': file_upload_failed,
    })
