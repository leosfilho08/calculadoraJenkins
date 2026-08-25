pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Instalar Dependências') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Análise Estática de Código (Flake8)') {
            steps {
                sh 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics'
            }
        }

        stage('Executar Testes Automatizados') {
            steps {
                sh 'pytest'
            }
        }
    }

    post {
        success {
            echo ' Pipeline finalizada com SUCESSO! Todos os testes passaram.'
        }
        failure {
            echo ' A pipeline FALHOU. Verifique os erros acima.'
        }
    }
}
