id="lz7fn2"
import qrcode
import io

class PixService:
    def __init__(self):
        # Sua chave cadastrada no sistema
        self.chave_pix = "ce023233@gmail.com"
        self.beneficiario = "GuildControl Admin"
        self.cidade = "Imperatriz"

    def gerar_copia_e_cola(self, valor):
        """Retorna o código Pix Copia e Cola formatado para o banco"""
        # Formata o valor com duas casas decimais
        valor_str = f"{valor:.2f}".replace(" ", "")
        len_valor = f"{len(valor_str):02d}"
        
        # Estrutura estática básica de um payload Pix padrão
        payload = (
            "00020101021226580014br.gov.bcb.pix0119"
            f"{self.chave_pix}52040000530398654"
            f"{len_valor}{valor_str}5802BR5918"
            f"{self.beneficiario}6010"
            f"{self.cidade}62070503***6304"
        )
        return payload

    def gerar_qr_code(self, valor):
        """Gera a imagem do QR Code para o usuário escanear na tela"""
        payload = self.gerar_copia_e_cola(valor)
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(payload)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        output = io.BytesIO()
        img.save(output, format="PNG")
        return output.getvalue()
