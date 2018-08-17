# coding=utf8
# Klasse Vehicle
class vehicle(object):
    def __init__(self, brand, model, kilometers, general_service_date):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.general_service_date = general_service_date

    def get_car(self):
        return self.brand +" "+ self.model


# Funktion Alle Vehicle anzeigen
def show_all_vehicles(vehicles):
    # ES IST NOTWENDIG ENUMERATE ANZUGEBEN, WENN DER EINGABEPARAMETER EINE LISTE IST.
    for index, singleVehicle in enumerate(vehicles):
        print(">")
        print("> System-ID = " + str(index))
        print("> " + singleVehicle.get_car())
        print("> " +singleVehicle.kilometers)
        print("> " +singleVehicle.general_service_date)
        print(">")
    if not vehicles:
        print("> Es sind aktuell keine Fahrzeuge angelegt.")
        print("> Bitte legen Sie in FORG Fahrzeuge an.")
        print(">")


# Funktion Neues Vehicle hinzufügen
def add_new_vehicle(vehicles):
    brand = raw_input("> Gib die Automarke ein: ")
    model = raw_input("> Gib das Modell des Autos ein: ")
    kilometers = raw_input("> Gib den aktuellen Kilometerstand ein: ")
    general_service_date = raw_input("> Gib das Datum des TÜVs ein: ")

    new = vehicle(brand=brand, model=model, kilometers=kilometers, general_service_date=general_service_date)
    vehicles.append(new)

    print(">")
    print("> " + new.get_car() + " wurde hinzugefügt.")
    print(">")


# Funktion Edit Vehicle => Kilometer, General Service
def edit_vehicle(vehicles):
    for index, singleVehicle in enumerate(vehicles):
        print("> ID: " + str(index) + " | " + singleVehicle.get_car())
    if not vehicles:
        print("> Es sind aktuell keine Fahrzeuge angelegt.")
        print("> Bitte legen Sie in FORG Fahrzeuge an.")
        print(">")
    else:
        selection = raw_input("> Wähle per ID das Auto aus, dass bearbeitet werden soll.")
        selected_vehicle = vehicles[int(selection)]

        newkilometers = raw_input("> Gib den neuen Kilometerstand ein: ")
        selected_vehicle.kilometers = newkilometers

        newgeneral_service_date = raw_input("> Gib das neue Datum des TÜVs ein: ")
        selected_vehicle.general_service_date = newgeneral_service_date

        print(">")
        print("> Fahrzeug " + selected_vehicle.get_car() + " wurde bearbeitet.")
        print(">")


# Funktion Daten speichern
def saveData(vehicles):
    data = open("forg_results.txt", "w+")
    data.write("Fahrzeugbestand: \n")
    data.write("")
    for singleVehicle in vehicles:
        data.write(singleVehicle.brand + "\n")
        data.write(singleVehicle.model + "\n")
        data.write(singleVehicle.kilometers + "\n")
        data.write(singleVehicle.general_service_date + "\n")
        data.write("\n")
    data.close()
    print("> Alle Ergebnisse wurden in eine Datei gespeichert.")
    print(">")


# Funktion MAIN
def main():
    vehicles = []
    print(">")
    print("> Herzliche willkommen in ihrem Fahrzeug Organisations Programm FORG")
    print(">")
    while True:
        print("> Hauptmenü:")
        print("> a) Alle Fahrzeuge anzeigen")
        print("> b) Neues Fahrzeug hinzufügen")
        print("> c) Fahrzeug bearbeiten")
        print("> d) Daten speichern")
        print("> e) Programm verlassen")
        print(">")
        selection = raw_input("> Welche Operation wollen Sie durchführen? a), b), c), d) oder e) ").lower()
        selection = selection.replace(")","")

        if selection == "a":
            print(">")
            print("> Aktueller Fahrzeugbestand: ")
            print(">")
            show_all_vehicles(vehicles)
        elif selection == "b":
            print(">")
            add_new_vehicle(vehicles)
        elif selection == "c":
            print(">")
            edit_vehicle(vehicles)
        elif selection == "d":
            print(">")
            saveData(vehicles)
        elif selection == "e":
            print(">")
            print("> FORG wünscht Ihnen einen erfolgreichen Arbeitstag!")
            print("> FORG wünscht Ihnen Auf Wiedersehen! =)")
            break


if __name__ == '__main__':
    main()