import os
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from Algoritmos.analisis import ExcelProcessor
from django.conf import settings
import sweetify

class IndexView(TemplateView):
    template_name = 'ListasRetrasadas/listasretrasadas.html'

    def dispatch(self, request, *args, **kwargs):
        # Eliminar todos los archivos de la carpeta media al entrar en la vista
        media_path = settings.MEDIA_ROOT
        for filename in os.listdir(media_path):
            file_path = os.path.join(media_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('csv_file')
        if file:
            # Guardar el archivo en una ubicación temporal en la carpeta media
            file_path = os.path.join(settings.MEDIA_ROOT, 'temp_file.csv')
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            # Mostrar mensaje de procesamiento utilizando SweetAlert
            sweetify.info(request, 'Procesando archivo, por favor espere...')

            # Procesar el archivo CSV
            processor = ExcelProcessor(file_path)
            try:
                processed_file_url = processor.process_csv()
                download_url = processor.download_excel()
                # Mostrar mensaje de éxito utilizando SweetAlert
                sweetify.success(request, 'Archivo procesado exitosamente', button='OK')
                return render(request, self.template_name, {'processed_file_url': processed_file_url, 'download_url': download_url})
            except Exception as e:
                # Mostrar mensaje de error utilizando SweetAlert
                sweetify.error(request, f'Error al procesar el archivo: {str(e)}', persistent=True)
                return redirect('index')  # Redirigir a la página principal en caso de error
        else:
            # Mostrar mensaje de error utilizando SweetAlert
            sweetify.error(request, 'No se proporcionó ningún archivo CSV', persistent=True)
            return redirect('index')  # Redirigir a la página principal si no se proporciona un archivo
