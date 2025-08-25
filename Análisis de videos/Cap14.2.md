# Capítulo 14 – Máquinas Virtuales (Parte 2)

## 1. Virtualización con Contenedores

- Docker popularizó la virtualización ligera mediante contenedores.
- Antes se necesitaban muchas máquinas virtuales para múltiples servicios; ahora se puede crear una sola VM y dentro de ella desplegar cientos de servicios en contenedores.
- Linux Containers (LXC/LXD) ya existían, pero eran complejos; Docker los hizo amigables y accesibles.

---

## 2. Retos del Software de Virtualización

La virtualización ha tomado décadas de desarrollo y aún enfrenta grandes desafíos para quienes diseñan estos sistemas.

### Procesador (CPU)

- En hipervisores tipo 2:
  - El sistema operativo anfitrión gestiona el CPU y el hipervisor hace llamadas a él.
- En hipervisores tipo 1:
  - El hipervisor accede directamente al hardware y administra la planificación de procesadores.

### Estrategias de gestión del CPU

- **Emulación**:
  - El hipervisor simula un procesador virtual.
  - Ejemplo: Android Emulator.
  - Desventaja: mucho más lento.
- **Coordinación directa**:
  - El hipervisor asigna segmentos de tiempo en procesadores físicos a las VMs.
  - Más eficiente, sin emulación.

---

## 3. Buenas Prácticas en Configuración de CPU

- Evitar asignar más procesadores virtuales de los necesarios.
- **Mala práctica**: al migrar de físico a virtual, duplicar la cantidad de CPUs pensando que se perderá eficiencia.
- **Recomendación**:
  - Comenzar con pocos vCPUs (1–2).
  - Aumentar solo si la aplicación realmente lo requiere.
- Problema:
  - Cuantos más vCPUs se configuren, más difícil es para el hipervisor encontrar espacio en pCPUs libres.

---

## 4. Administración de Memoria

El hipervisor también debe gestionar la memoria RAM, aplicando estrategias de optimización:

### Estrategias principales

- **Memory Sharing (páginas compartidas)**:

  - Si varias VMs usan el mismo SO y programas, en lugar de duplicar en RAM, se enlazan a las mismas páginas de memoria.

- **Thin Provisioning (aprovisionamiento fino)**:

  - Se configura una VM con cierta cantidad de RAM/almacenamiento, pero solo se asigna lo que realmente utiliza.

- **Ballooning**:

  - El hipervisor puede reclamar memoria no usada de una VM y reasignarla a otra.

- **Memory Overcommit**:
  - Se pueden asignar más recursos virtuales (RAM y CPUs) de los que existen físicamente.
  - Funciona mientras no todas las VMs demanden su máximo simultáneamente.
  - Riesgo: si todas lo hacen, se generan errores y fallos.
  - Analogía: como un banco que presta más dinero del que realmente tiene, confiando en que no todos retirarán al mismo tiempo.

---

## Conclusion

- Los contenedores son una alternativa ligera y complementaria a las máquinas virtuales.
- La eficiencia de la virtualización depende de la gestión inteligente de CPU y RAM por parte del hipervisor.
- Buenas prácticas de configuración (no sobreasignar CPUs o RAM sin justificación) son esenciales para evitar cuellos de botella y mantener el rendimiento.
- La optimización de recursos mediante técnicas como memory sharing, thin provisioning y ballooning permite aprovechar al máximo la infraestructura física.
