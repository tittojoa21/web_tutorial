from django.test import TestCase

class MyTestCase(TestCase):
    def test_registro_exitoso(self):
        response = self.client.get('registro_gym_view')  
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Registro Exitoso')
        self.assertContains(response, 'Tu registro ha sido exitoso. ¡Gracias por registrarte!')

    def test_formulario_registro(self):
        response = self.client.get('registro_gym_view')  
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Registro de Gimnasio')
        self.assertContains(response, '<form')
        self.assertContains(response, 'id_nombre')
        self.assertContains(response, 'id_email')
        self.assertContains(response, 'id_password1')
        self.assertContains(response, 'id_password2')
        self.assertContains(response, '<button')

    def test_estilo_pagina(self):
        response = self.client.get('registro_gym_view')  
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'background-color: #f0f0f0;')
        self.assertContains(response, 'color: #333;')
        self.assertContains(response, 'background-color: #4CAF50;')
        self.assertContains(response, 'color: white;')
    
