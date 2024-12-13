import ROOT
import sys

file_path = "CAFAFB30-8522-E540-A71A-502B435962A0.root"

print("Opening the ROOT file: {}".format(file_path))
file = ROOT.TFile.Open(file_path)

if not file or file.IsZombie():
    print("Error: Cannot open file {}".format(file_path))
    sys.exit(1)

tree = file.Get("Events")
if not tree:
    print("Error: 'Events' tree not found.")
    file.Close()
    sys.exit(1)

generator_branch_name = "GenEventInfoProduct_generator__GEN.obj"

if not tree.GetBranch(generator_branch_name):
    print("Error: Branch '{}' not found in 'Events' tree.".format(generator_branch_name))
    file.Close()
    sys.exit(1)

n_events = 1

print("\nExtracting weights for the first {} events:".format(n_events))
print("=" * 80)

for i in range(n_events):
    tree.GetEntry(i)
    print("Event {}:".format(i))
    
    # Access the weights from GenEventInfoProduct
    try:
        generator = getattr(tree, generator_branch_name)
        
        nominal_weight = generator.weight()
        print("  Weight from 'weight': {}".format(nominal_weight))
        
        # Extract the vector of weights
        weights = generator.weights()
        print("  Weight from 'weights' (Total {}):".format(len(weights)))
        for j, weight in enumerate(weights):
            print("    [{}]: {}".format(j, weight))
    except AttributeError as e:
        print("  Error accessing weights: {}".format(e))
    
    print("-" * 80)

file.Close()
print("\nExtraction complete.")

