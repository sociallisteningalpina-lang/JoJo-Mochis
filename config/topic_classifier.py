#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""
import re
from typing import Callable

def create_topic_classifier() -> Callable[[str], str]:
    """
    Retorna una función de clasificación de temas personalizada para la campaña JojoMochis.
    
    Returns:
        function: Función que toma un comentario (str) y retorna un tema (str)
    
    Usage:
        classifier = create_topic_classifier()
        tema = classifier("¿Dónde puedo comprar los JojoMochis?")
        # tema = 'Disponibilidad y Puntos de Venta'
    """
    
    def classify_topic(comment: str) -> str:
        """
        Clasifica un comentario en un tema específico basado en patrones regex.
        
        Args:
            comment: Texto del comentario a clasificar
            
        Returns:
            str: Nombre del tema asignado
        """
        comment_lower = str(comment).lower()
        
        # CATEGORÍA 1: Disponibilidad y Puntos de Venta
        if re.search(
            r'd[oó]nde|dónde se consiguen|d[oó]nde los puedo|d[oó]nde se encuentran|'
            r'no los encuentro|no han llegado|no llega|no venden|no hay|'
            r'mi tienda|mi pueblo|mi cerro|barrio|guaviare|cali|cartagena|ecuador|'
            r'punto de venta|[oó]xxo|env[ií]a|tiendita|mercanc[ií]a|surtido|'
            r'cu[aá]ndo llegan|cu[aá]ndo salen|ya salieron|todav[ií]a no',
            comment_lower
        ):
            return 'Disponibilidad y Puntos de Venta'
        
        # CATEGORÍA 2: Precio y Costo
        if re.search(
            r'precio|cu[aá]nto|caro|barato|vale|cobran|'
            r'2\.?000|3\.?000|3\.?500|4\.?000|bajenle el precio|'
            r'millonarios|garra|vendedor',
            comment_lower
        ):
            return 'Precio y Costo'
        
        # CATEGORÍA 3: Colección y Completitud
        if re.search(
            r'colecci[oó]n|completar|completa|todos los|falt[aóo]|'
            r'no he terminado|repetidos|conseguí|cu[aá]ntos son|'
            r'cu[aá]ntos motivos|apenas|solo tengo|tengo \d+|'
            r'primera edici[oó]n|todas las colecciones',
            comment_lower
        ):
            return 'Colección y Completitud'
        
        # CATEGORÍA 4: Solicitud de Información
        if re.search(
            r'nombres|listado|lista|cu[aá]les son|parte 2|'
            r'muestra|muestren|ense[ñn]a|video|'
            r'tarjeta|identificar|vienen con',
            comment_lower
        ):
            return 'Solicitud de Información'
        
        # CATEGORÍA 5: Opinión Positiva sobre los JojoMochis
        if re.search(
            r'lindos|hermosos|divinos|bellos|tiernos|amo|encanta|'
            r'me gusta|adoro|quiero todos|los necesito|feliz|'
            r'mejor|✨|❤|💕|🎄',
            comment_lower
        ):
            return 'Opinión Positiva sobre los JojoMochis'
        
        # CATEGORÍA 6: Personajes Favoritos
        if re.search(
            r'lucerita|estrella|pepetin[ao]|renny|elfo|ciervito|'
            r'guirnalda|bota|favorito|m[aá]s quería',
            comment_lower
        ):
            return 'Personajes Favoritos'
        
        # CATEGORÍA 7: Comparación con Colecciones Anteriores
        if re.search(
            r'mochisaurios|ilumimochis|mochizippis|mini ilumimochis|'
            r'primeros|originales|dinosaurios|dino|antes|anterior|'
            r'despu[eé]s de|primera colección|acuamochis|animals',
            comment_lower
        ):
            return 'Comparación con Colecciones Anteriores'
        
        # CATEGORÍA 8: Problemas con el Producto
        if re.search(
            r'da[ñn]|feo|mal pintado|sin|no tiene|se aplasta|'
            r'no alumbran|sin carita|sin la tirita|perdi|'
            r'robar|problema|no viene',
            comment_lower
        ):
            return 'Problemas con el Producto'
        
        # CATEGORÍA 9: Sorteos y Concursos
        if re.search(
            r'ganador|sorteo|cajas|cajitas|concurso|gan[eé]|'
            r'cu[aá]ndo anuncian|qui[eé]n gan[oó]|prontooo',
            comment_lower
        ):
            return 'Sorteos y Concursos'
        
        # CATEGORÍA 10: Interacción con Gaby (Community Manager)
        if re.search(
            r'gaby|gabi|gabyy|mejor practicante|contenido|'
            r'ya te sigo|siguenos|suscr|apoyen',
            comment_lower
        ):
            return 'Interacción con Community Manager'
        
        # CATEGORÍA 11: Solicitudes de Productos o Regalos
        if re.search(
            r'regalame|reg[aá]lame|env[ií]a|manda|paquete gratis|'
            r'alpina dame|quiero para mi casa|me los llevas',
            comment_lower
        ):
            return 'Solicitudes de Productos'
        
        # CATEGORÍA 12: Características del Producto
        if re.search(
            r'silicona|estirable|hilo|colgar|pl[aá]stico|'
            r'calendario de adviento|[aá]rbol|decorar',
            comment_lower
        ):
            return 'Características del Producto'
        
        # CATEGORÍA 13: Fuera de Tema / Spam
        if re.search(
            r'aaaaaaa+|hola a aaaa|jajaja+|❤️|✨|plis|pliss|porfa+',
            comment_lower
        ) and len(comment_lower.split()) <= 3:
            return 'Fuera de Tema / Spam'
        
        # Si tiene emojis solos o comentarios muy cortos
        if len(comment_lower.strip()) < 10 or comment_lower.strip() in ['si', 'no', 'ok', 'a', 'k', '★']:
            return 'Fuera de Tema / Spam'
        
        # CATEGORÍA DEFAULT: Otros
        return 'Otros'
    
    return classify_topic
# ============================================================================
# METADATA DE LA CAMPAÑA (OPCIONAL)
# ============================================================================

CAMPAIGN_METADATA = {
    'campaign_name': 'Alpina - Kéfir',
    'product': 'Kéfir Alpina',
    'categories': [
        'Preguntas sobre el Producto',
        'Comparación con Kéfir Casero/Artesanal',
        'Ingredientes y Salud',
        'Competencia y Disponibilidad',
        'Opinión General del Producto',
        'Fuera de Tema / No Relevante',
        'Otros'
    ],
    'version': '1.0',
    'last_updated': '2025-11-20'
}


def get_campaign_metadata() -> dict:
    """Retorna metadata de la campaña"""
    return CAMPAIGN_METADATA.copy()
