pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verificar Sintaxe Python') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m py_compile *.py || python -m py_compile *.py'
                    } else {
                        bat 'python -m py_compile *.py'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Build finalizado com sucesso!'
        }
        failure {
            echo 'Falha na verificação do código. Cheque o Console Output.'
        }
    }
}
