# Laboratorio #2 – Contenedores

**Curso:** BIT-28 Sistemas Operativos II  
**Universidad Latina de Costa Rica**

---

## Objetivos

- Comprender qué son los contenedores
- Diferenciar entre Docker y LXD
- Instalar y configurar Docker en Ubuntu
- Administrar contenedores Docker
- Gestionar contenedores con interfaz gráfica Portainer

---

## 1. ¿Qué son los contenedores?

La virtualización tradicional (ej. VirtualBox, VMWare, KVM) permite crear múltiples máquinas virtuales en un mismo servidor físico, pero con un costo de recursos mayor (CPU, RAM, disco asignados que a veces no se usan)

Los contenedores, en cambio:

- Comparten el kernel del host en lugar de virtualizar un SO completo
- Son aislados entre sí y del host
- Cada contenedor suele tener un único propósito
- Usan solo los recursos que necesitan → mayor eficiencia

Analogía: Una VM es como una casa independiente, un contenedor es como un apartamento en un edificio: comparte infraestructura, pero está aislado de los demás.

---

## 2. Docker vs LXD

- **LXC/LXD**

  - Basado en Linux Containers.
  - Se asemeja más a una máquina virtual ligera.
  - Permite snapshots y migración.
  - Muy usado en entornos Linux.

- **Docker**
  - Orientado a contenedores de aplicaciones.
  - Popular por su facilidad de uso y ecosistema (Docker Hub).
  - Funciona en Linux, macOS y Windows.
  - Uso transaccional: cada capa es independiente y reutilizable.

---

## 3. Instalación de Docker

En Ubuntu 20.04/22.04 seguir la guía oficial:  
[Docker Install Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

Verificar instalación:

```bash
docker --version
```
