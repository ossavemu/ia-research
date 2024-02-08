import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def get_files():
    # Obtiene la ruta al directorio del script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Combina la ruta del script con el directorio 'blog'
    blog_dir = os.path.join(script_dir, 'blog')
    
    # Lista todos los archivos .md en el directorio 'blog'
    files = [os.path.join(blog_dir, file) for file in os.listdir(blog_dir) if file.endswith('.md')]
    
    return files

def get_content(files):
    content = ''
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:  # Agrega encoding='utf-8' para manejar caracteres especiales
            content += f.read()
    return content

def write_resume(content):
    try:
        with open('resume.txt', 'w', encoding='utf-8') as f:
            f.write(content)
        print("El archivo 'resume.txt' se creó correctamente.")
    except Exception as e:
        print(f"Error al escribir el archivo 'resume.txt': {e}")

files = get_files()
content = get_content(files)
print(content)
write_resume(content)
