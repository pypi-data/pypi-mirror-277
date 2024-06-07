


def edit_docker_compose(file_path):
    import yaml
    with open(file_path, 'r') as file:
        docker_compose = yaml.safe_load(file)

    # Hier können Sie die Änderungen an der docker-compose.yaml-Datei vornehmen
    # Zum Beispiel können Sie einen neuen Service hinzufügen
    docker_compose['services']['new_service'] = {
        'image': 'new_image',
        'ports': ['8080:80']
    }

    with open(file_path, 'w') as file:
        yaml.dump(docker_compose, file, default_flow_style=False)

