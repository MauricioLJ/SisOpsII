# Capítulo 14 – Virtualización

## 1. Contexto histórico y concepto

- **Antes**: un servidor físico corría un único sistema operativo y servicios.
  - Problema: si fallaba el hardware ya fuera la tarjeta de red, fuente, etc, todo el sistema quedaba inactivo por días.
- **Ahora**: gracias a la virtualización, si una máquina falla puede trasladarse a otra con alta disponibilidad.
- **Concepto central**: la virtualización es ejecutar servicios, aplicaciones o sistemas sin depender directamente del hardware físico.

---

## 2. Ventajas

- **Multiplicidad**: correr varios sistemas operativos en un solo servidor.
- **Mantenimiento ágil**: levantar un backup o clonar una VM es más rápido que reparar físicamente.
- **Versatilidad**: optimiza el uso de CPU, RAM y almacenamiento en un mismo equipo.
- **Consolidación**: permite reducir la cantidad de servidores físicos → ahorro de energía.
- **Agregación de recursos**: añadir más memoria, CPU o almacenamiento al cluster de forma flexible.
- **Alta disponibilidad**: despliegue en distintas regiones; si una cae, otra asume.

---

## 3. Hipervisores

El hipervisor es la capa de software que gestiona las máquinas virtuales sobre el hardware.

### Tipos:

- Bare-metal: se instala directamente en el hardware, funcionando como un sistema operativo especializado.
  - Ejemplos: VMware ESXi, Microsoft Hyper-V,, Citrix XenServer.
- Hosted: este se instala sobre un sistema operativo existente.
  - Ejemplos: VirtualBox, VMware Workstation.

---

## 4. Funciones del hipervisor

- Administrar la ejecución de máquinas virtuales.
- Realizar emulación de dispositivos
- Controlar privilegios de procesos invitados.
- Gestionar el ciclo de vida de las VMs: creación, ejecución, snapshots, eliminación.
- Mantener actualizaciones y seguridad.
- Optimizar hardware: drivers especializados para servidores soportados.

---

## 5. Técnicas de virtualización

- **Paravirtualización**:
  - Modifica drivers invitados para comunicarse más rápido con el hipervisor o hardware.
  - Aumenta el rendimiento.
- **Asistencia por hardware**:
  - Extensiones en procesadores (Intel VT-x, AMD-V) aceleran operaciones de virtualización.
  - Se habilitan normalmente desde el BIOS/UEFI.

---

## 6. Conceptos clave

- **Driver**: software dentro del sistema operativo que habla con el hardware.
- **Controlador**: chip o software embebido que controla directamente el dispositivo físico.

La paravirtualización requiere adaptar drivers para hablar con el hipervisor/hardware de forma más eficiente.

---

## 7. Appliances virtuales

- Son imágenes listas para usar (ej. en AWS o Azure) que permiten desplegar una VM con sistema operativo y aplicaciones en segundos, sin necesidad de instalación manual.

---

## Conclusión

La virtualización transformó la informática moderna:

- **Mayor disponibilidad** (fallos de hardware ya no implican caída del servicio).
- **Eficiencia energética y de recursos** (consolidación y agregación dinámica).
- **Flexibilidad y escalabilidad** (despliegues rápidos, movilidad de cargas).
