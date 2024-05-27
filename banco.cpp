#include <iostream>
#include <fstream> 
#include <string>
#include <vector>
using namespace std;

// Estructuras
struct Cuenta {
    string tipo_cuenta;
    long long int num_cuenta;
};

struct Cliente {
    string nombre;
    long long int num_doc;
    Cuenta info_cuenta;
    long long int saldo;
};

// Sobrecarga del operador << para la struct Cliente
ostream& operator<<(ostream& os, const Cliente& cliente) {
    os << "Nombre: " << cliente.nombre << "\n"
       << "Numero de documento: " << cliente.num_doc << "\n"
       << "Numero de cuenta: " << cliente.info_cuenta.num_cuenta << "\n"
       << "Tipo de cuenta: " << cliente.info_cuenta.tipo_cuenta << "\n"
       << "Saldo: " << cliente.saldo << "\n";
    return os;
}

// Función para agregar nuevos clientes y crear archivos de texto
void agregarClientes(vector<Cliente>& clientes, int n) {
    for (int i = 0; i < n; ++i) {
        Cliente c;
        cout << "Nombre del cliente " << i + 1 << ": ";
        cin.ignore();
        getline(cin, c.nombre);
        cout << "Numero de documento del cliente " << i + 1 << ": ";
        cin >> c.num_doc;
        cout << "Numero de cuenta del cliente " << i + 1 << ": ";
        cin >> c.info_cuenta.num_cuenta;
        cin.ignore(); // Ignorar el salto de línea que queda en el buffer
        cout << "Tipo de cuenta del cliente " << i + 1 << ": ";
        getline(cin, c.info_cuenta.tipo_cuenta);
        cout << "Saldo del cliente " << i + 1 << ": ";
        cin >> c.saldo;
        clientes.push_back(c);

        // Crear archivo de texto para el cliente
        ofstream archivo("cliente" + to_string(i + 1) + ".txt");
        if (archivo.is_open()) {
            archivo << "Nombre: " << c.nombre << "\n";
            archivo << "Numero de documento: " << c.num_doc << "\n";
            archivo << "Numero de cuenta: " << c.info_cuenta.num_cuenta << "\n";
            archivo << "Tipo de cuenta: " << c.info_cuenta.tipo_cuenta << "\n";
            archivo << "Saldo: " << c.saldo << "\n";
            archivo.close();
            cout << "Archivo de texto creado para el cliente " << i + 1 << endl;
        } else {
            cout << "Error al crear el archivo para el cliente " << i + 1 << endl;
        }

        cin.clear();

        system("cls");
    }
}

// Función para mostrar los clientes registrados
void mostrarClientes(const vector<Cliente>& clientes) {
    for (size_t i = 0; i < clientes.size(); i++) {
        cout << "Cliente " << i + 1 << ": \n" << clientes[i] << endl;
    }
}

// Función para realizar una transferencia entre dos clientes y actualizar los saldos en los archivos de texto
bool realizarTransferencia(vector<Cliente>& clientes, long long int num_cuenta_origen, long long int num_cuenta_destino, long long int monto) {
    
    Cliente* cliente_origen = nullptr;
    Cliente* cliente_destino = nullptr;

    // Buscar los clientes por número de cuenta
    for (Cliente& c : clientes) {
        if (c.info_cuenta.num_cuenta == num_cuenta_origen) {
            cliente_origen = &c;
        } else if (c.info_cuenta.num_cuenta == num_cuenta_destino) {
            cliente_destino = &c;
        }
        if (cliente_origen && cliente_destino) {
            break;
        }
    }

    // Verificar que ambos clientes existan y que el saldo sea suficiente
    if (cliente_origen && cliente_destino && cliente_origen->saldo >= monto) {
        cliente_origen->saldo -= monto;
        cliente_destino->saldo += monto;

        // Actualizar los archivos de texto con los nuevos saldos
        ofstream archivo_origen("cliente" + to_string(cliente_origen->info_cuenta.num_cuenta) + ".txt", ios::trunc);
        ofstream archivo_destino("cliente" + to_string(cliente_destino->info_cuenta.num_cuenta) + ".txt", ios::trunc);

        if (archivo_origen.is_open() && archivo_destino.is_open()) {
            archivo_origen << "Nombre: " << cliente_origen->nombre << "\n";
            archivo_origen << "Numero de documento: " << cliente_origen->num_doc << "\n";
            archivo_origen << "Numero de cuenta: " << cliente_origen->info_cuenta.num_cuenta << "\n";
            archivo_origen << "Tipo de cuenta: " << cliente_origen->info_cuenta.tipo_cuenta << "\n";
            archivo_origen << "Saldo: " << cliente_origen->saldo << "\n";
            archivo_origen.close();

            archivo_destino << "Nombre: " << cliente_destino->nombre << "\n";
            archivo_destino << "Numero de documento: " << cliente_destino->num_doc << "\n";
            archivo_destino << "Numero de cuenta: " << cliente_destino->info_cuenta.num_cuenta << "\n";
            archivo_destino << "Tipo de cuenta: " << cliente_destino->info_cuenta.tipo_cuenta << "\n";
            archivo_destino << "Saldo: " << cliente_destino->saldo << "\n";
            archivo_destino.close();

            return true;
        } else {
            cout << "Error al abrir los archivos para actualizar los saldos." << endl;
            return false;
        }
    }
    return false;
}

// Hilo principal
int main() {
    int op, n;
    vector<Cliente> clientes;

    do {
        cout << "1. Agregar cliente(s)" << endl;
        cout << "2. Mostrar cliente(s)" << endl;
        cout << "3. Realizar transferencia" << endl;
        cout << "4. Salir" << endl;
        cin >> op;

        switch (op) {
            case 1:
                // Se pregunta al usuario cuántos clientes va a agregar al vector de clientes
                cout << "Cuantos clientes desea agregar? ";
                cin >> n;

                // Se agregan los clientes al vector
                agregarClientes(clientes, n);
                break;

            case 2:
                // Se muestran los clientes registrados
                mostrarClientes(clientes);
                break;

            case 3: {
                // Realizar transferencia
                long long int num_cuenta_origen, num_cuenta_destino, monto;
                cout << "Numero de cuenta origen: ";
                cin >> num_cuenta_origen;
                cout << "Numero de cuenta destino: ";
                cin >> num_cuenta_destino;
                cout << "Monto a transferir: ";
                cin >> monto;

                if (realizarTransferencia(clientes, num_cuenta_origen, num_cuenta_destino, monto)) {
                    cout << "Transferencia realizada con exito." << endl;
                } else {
                    cout << "Error en la transferencia. Verifique los datos y el saldo." << endl;
                }
                break;
            }

            case 4:

                system("cls");
                cout << "Saliendo del programa..." << endl;
                exit(0);
                break;

            default:
                // Si la opcion seleccionada no está contemplada en los case se muestra que no es valida
                cout << "La opcion seleccionada no es valida" << endl;
                break;
        }

    } while (op != 4);

    return 0;
}
