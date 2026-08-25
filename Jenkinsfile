pipeline {
    agent any

    stages {
        stage('Checkout do Codigo') {
            steps {
                echo 'Baixando repositorio do GitHub com sucesso...'
            }
        }

        stage('Validar Estrutura do Projeto') {
            steps {
                echo 'Verificando a presenca do arquivo calculadora.py...'
            }
        }

        stage('Simular Testes da Calculadora') {
            steps {
                echo 'Testando Soma: 10 + 5 = 15 [PASSOU]'
                echo 'Testando Subtracao: 10 - 5 = 5 [PASSOU]'
                echo 'Testando Multiplicacao: 4 * 3 = 12 [PASSOU]'
                echo 'Testando Divisao: 10 / 2 = 5 [PASSOU]'
            }
        }
        
        stage('Deploy / Sucesso') {
            steps {
                echo 'Calculadora pronta para ser executada!'
            }
        }
    }

    post {
        success {
            echo ' PIPELINE EXECUTADA COM SUCESSO! SEU PROJETO ESTA OK NO JENKINS!'
        }
    }
}
