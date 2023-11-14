import pickle
import shelve
print("Pickling lists.\n")
print("Unpickling lists.")
variety = ["sweet", "hot" ,"dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz" ,"Ulassic"]
with open("pickles1.dat", "wb") as pickle_file:
    pickle.dump(variety, pickle_file)
    pickle.dump(shape, pickle_file)
    pickle.dump(brand, pickle_file)
with open("pickles1.dat", "rb") as pickle_file:
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
