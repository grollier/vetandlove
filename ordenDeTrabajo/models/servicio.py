#Create your models here
from django.db import models

from .ordenT import Orden

class Servicio(models.Model):
    CONSULTA = 'CONSULTA'
    EMERGENCIA = 'EMERGENCIA'
    DESPARASITACION = 'DESPARASITACION'
    VACUNAP = 'VACUNAP'
    VACUNAD = 'VACUNAD'
    VACUNAG = 'VACUNAG'
    INYECCION = 'INYECCION'
    LIMPIEZAD = 'LIMPIEZA'
    OTOHEMATOMA = 'OTOHEMATOMA'
    OVHELECTIVA = 'OVHELECTIVA'
    PIOMETRA = 'PIOMETRA'
    ORQUIECTOMIA = 'ORQUIECTOMIA'
    EUTANASIA = 'EUTANASIA'
    HEMATOLOGIA = 'HEMATOLOGIA'
    BILIRRUBINA = 'BILIRRUBINA'
    BILIRRUBINAD = 'BILIRRUBINAD'
    BILIRRUBINAI = 'BILIRRUBINAI'
    CALCIO = 'CALCIO'
    COLESTEROLT = 'COLESTEROLT'
    CREATININA = 'CREATININA'
    FOSFATAA = 'FOSFATAA'
    GLUCOSA = 'GLUCOSA'
    NITROGENOU = 'NITROGENOU'
    PROTEINAST = 'PROTEINAST'
    TGPALAT = 'TGP/ALAT'
    TGOASAT = 'TGO/ASAT'
    TRIGLICERIDOS = 'TRIGLICERIDOS'
    UREA = 'UREA'
    FIBRINOGENO = 'FIBRINOGENO'
    TPROTOMBINA = 'TPROTOMBINA'
    TTROMBOPLASTINA = 'TTROMBOPLASTINAT'
    T4LIBRE = 'T4LIBRE'
    ORINA = 'ORINA'

    servicioId = models.AutoField(primary_key=True)
    SERVICIOS_MASCOTA = (
            ('Consulta',(
                (CONSULTA, 'Consulta General'),
                (EMERGENCIA, 'Consulta de Emergencia'),
                (DESPARASITACION, 'Desparasitacion'),
                (VACUNAP, 'Vacunas Perro'),
                (VACUNAD, 'Vacuna + Desparasitacion'),
                (VACUNAG, 'Vacunas Gatos'),
                (INYECCION,'Inyeccion en consulta'),
                (LIMPIEZAD, 'Limpieza Denta'),
                (OTOHEMATOMA, 'Otohematoma'),
                (OVHELECTIVA, 'OVH electiva'),
                (PIOMETRA, 'Piometra'),
                (ORQUIECTOMIA, 'Orquiectomia'),
                (EUTANASIA, 'Eutanasia'),
                        ) 
            ),
            ('Prueba',(
                (HEMATOLOGIA, 'Hematologia'),
                (BILIRRUBINA, 'Bilirrubinas'),
                (BILIRRUBINAD, 'Bilirrubina Directa'),
                (BILIRRUBINAI, 'Bilirrubina Indirecta'),
                (CALCIO, 'Calcio'),
                (COLESTEROLT, 'Colesterol Total'),
                (CREATININA, 'Creatinina'),
                (FOSFATAA, 'Fosfata Alcalina'),
                (GLUCOSA, 'Glucosa'),
                (NITROGENOU, 'Nitrogeno de Urea'),
                (PROTEINAST, 'Proteinas Totales'),
                (TGPALAT, 'TGP/ALAT'),
                (TGOASAT, 'TGO/ASAT'),
                (TRIGLICERIDOS, 'Trigliceridos'),
                (UREA, 'Urea'),
                (FIBRINOGENO, 'Fibrinogeno'),
                (TPROTOMBINA, 'Tiempo de Protombina'),
                (TTROMBOPLASTINA, 'Tiempo de Tromboplastina'),
                (T4LIBRE, 'T4 Libre'),
                (ORINA, 'Orina'),
                      )
            ),
    )
    servicios = models.CharField(
        max_length= 20,
        choices= SERVICIOS_MASCOTA,
        help_text='Elija un servicio para la mascota',
    )

    def __str__(self):
        return self.servicios

    precio_servicio = models.DecimalField(max_digits=6, decimal_places=2,blank=True, help_text='Ingrese el precio del servicio',)
    ordenes = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='servicio_ordenes',default=False)
