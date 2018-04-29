from unittest import TestCase

from oo.carro import Motor, Direcao, Carro


class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
        motor.acelerar()
        self.assertEqual(2, motor.velocidade)
        motor.acelerar()
        self.assertEqual(3, motor.velocidade)

    def test_frear(self):
        motor = Motor()
        motor.acelerar()
        motor.acelerar()
        motor.acelerar()
        self.assertEqual(3, motor.velocidade)
        motor.frear()
        self.assertEqual(1, motor.velocidade)
        motor.frear()
        self.assertEqual(0, motor.velocidade)

    def test_direcao_inicial(self):
        direcao = Direcao()
        self.assertEqual('Norte', direcao.valor)

    def test_girar_direcao_a_direita(self):
        direcao = Direcao()
        direcao.girar_a_direita()
        self.assertEqual('Leste', direcao.valor)
        direcao.girar_a_direita()
        self.assertEqual('Sul', direcao.valor)
        direcao.girar_a_direita()
        self.assertEqual('Oeste', direcao.valor)
        direcao.girar_a_direita()
        self.assertEqual('Norte', direcao.valor)

    def test_griar_direcao_a_esquerda(self):
        direcao = Direcao()
        direcao.girar_a_esquerda()
        self.assertEqual('Oeste', direcao.valor)
        direcao.girar_a_esquerda()
        self.assertEqual('Sul', direcao.valor)
        direcao.girar_a_esquerda()
        self.assertEqual('Leste', direcao.valor)
        direcao.girar_a_esquerda()
        self.assertEqual('Norte', direcao.valor)

    def test_carro_velocidade_inicial(self):
        motor = Motor()
        direcao = Direcao()
        carro = Carro(direcao, motor)
        self.assertEqual(0, carro.calcular_velocidade())

    def test_carro_acelerar(self):
        motor = Motor()
        direcao = Direcao()
        carro = Carro(direcao, motor)
        carro.acelerar()
        self.assertEqual(1, carro.calcular_velocidade())
        carro.acelerar()
        self.assertEqual(2, carro.calcular_velocidade())

    def test_carro_frear(self):
        motor = Motor()
        direcao = Direcao()
        carro = Carro(direcao, motor)
        carro.acelerar()
        carro.acelerar()
        carro.frear()
        self.assertEqual(0, carro.calcular_velocidade())

    def test_carro_direcao_inicial(self):
        motor = Motor()
        direcao = Direcao()
        carro = Carro(direcao, motor)
        self.assertEqual('Norte', carro.calcular_direcao())

    def test_carro_girar_a_direita(self):
        motor = Motor()
        direcao = Direcao()
        carro = Carro(direcao, motor)
        carro.girar_a_direita()
        self.assertEqual('Leste', carro.calcular_direcao())
        carro.girar_a_direita()
        self.assertEqual('Sul', carro.calcular_direcao())
        carro.girar_a_direita()
        self.assertEqual('Oeste', carro.calcular_direcao())
        carro.girar_a_direita()
        self.assertEqual('Norte', carro.calcular_direcao())

    def test_carro_girar_a_esquerda(self):
        motor = Motor()
        direcao = Direcao()
        carro = Carro(direcao, motor)
        carro.girar_a_esquerda()
        self.assertEqual('Oeste', carro.calcular_direcao())
        carro.girar_a_esquerda()
        self.assertEqual('Sul', carro.calcular_direcao())
        carro.girar_a_esquerda()
        self.assertEqual('Leste', carro.calcular_direcao())
        carro.girar_a_esquerda()
        self.assertEqual('Norte', carro.calcular_direcao())