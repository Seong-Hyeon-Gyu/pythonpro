import pickle
import shelve
print("Pickling lists.\n")
variety = ["sweet", "hot" ,"dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz" ,"Ulassic"]
pickle_file = open("pickles1.dat", "wb")
pickle.dump(variety, pickle_file)
pickle.dump(shape, pickle_file)
pickle.dump(brand, pickle_file)
pickle_file.close()
pickle_file = open("pickles1.dat", "r")
variety = pickle.load(pickle_file)
shape = pickle.load(pickle_file)
brand = pickle.load(pickle_file)
print(variety)
print(shape)
print(brand)
print("\nShelving lists.\n")
print("Restriveing the lists from a shelved files:")
pickles = shelve.open("pickles2.dat")
pickles["variety"]=["sweet", "hot", "dill"]
pickles["shape"]=["whole", "spear", "chip"]
pickles["brand"]=["Claussen", "Heinz", "Ulassic"]
pickles.sync()
for key in pickles.keys():
    print(key, "-", pickles[key])
