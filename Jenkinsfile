pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verificar Ambiente Python') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 --version || python --version'
                    } else {
                        bat 'python --version'
                    }
                }
            }
        }

        stage('Validar Sintaxe') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m py_compile calculadora.py test_calculadora.py'
                    } else {
                        bat 'python -m py_compile calculadora.py test_calculadora.py'
                    }
                }
            }
        }

        stage('Executar Testes Unitários') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m unittest test_calculadora.py'
                    } else {
                        bat 'python -m unittest test_calculadora.py'
                    }
                }
            }
        }

        stage('Executar Backend (CLI)') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 calculadora.py soma 20 30'
                    } else {
                        bat 'python calculadora.py soma 20 30'
                    }
                }
            }
        }
    }

    post {
        success {
            echo ' PIPELINE BACKEND EXECUTADA COM SUCESSO!'
        }
        failure {
            echo ' FALHA NA PIPELINE BACKEND. Verifique o Console Output.'
        }
    }
}
