from servicios import Servicios
import discord


class InterfazDiscord:
    def __init__(self):
        self.servicios = Servicios()

    def respuesta_para(self, mensaje = '', archivo = ''):
        respuesta = {}
        respuesta['mensaje'] = mensaje
        if archivo:
            respuesta['archivo'] = discord.File(archivo)
        else:
            respuesta['archivo'] = None
        return respuesta

    def precio_del_dolar(self, ctx, *args):
        valor = self.servicios.precio_del_dolar()
        mensaje = f'${valor}'
        return self.respuesta_para(mensaje = mensaje)

    def precio_del_pase_fortnite(self, ctx, *args):
        valor = self.servicios.precio_del_pase_fortnite()
        mensaje = f'${valor} + imp = ${valor * 1.6}'
        return self.respuesta_para(mensaje = mensaje)

    def minecraft_server_status(self, ctx, *args):
        data = self.servicios.minecraft_server_status()
        mensaje = 'Servidor encendido' if data['online'] else 'Servidor apagado'

        mensaje += f', {len(data["jugadores"])} online:'

        for jugador in data['jugadores']:
            mensaje += f'\n    {jugador}'
        
        return self.respuesta_para(mensaje = mensaje)

    def iniciar_minecraft_server(self, ctx, *args):
        resultado = self.servicios.iniciar_minecraft_server()
        mensaje = f'{resultado}'
        return self.respuesta_para(mensaje = mensaje)
    
    def mensajovich(self, ctx, *args):
        mensaje = self.servicios.mensajovich()
        return self.respuesta_para(mensaje = mensaje)
    
    def iniciar_files_server(self, ctx, *args):
        resultado = self.servicios.iniciar_files_server()
        mensaje = f'{resultado}'
        return self.respuesta_para(mensaje = mensaje)
    