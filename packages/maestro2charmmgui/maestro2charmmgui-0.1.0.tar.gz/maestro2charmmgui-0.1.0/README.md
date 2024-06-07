# Maestro2CharmmGUI

Check whether it works:

```bash
cd maestro2charmmgui
pytest

# 2 passed, 1 warnining
```

For usage, see the [jupyter notebook](./rename_Hs.ipynb) for renaming the hydrogens defined in Maestro into CHARMM's definition. 

```python
from maestro2charmmgui.rename import transform_resname

# rename the atoms by using a residue-based corresponding dictionary with a single function
input = "path/to/pdbfile.pdb"
output = "path/to/pdbfile_charmm.pdb"

transform_with_resname(input, output)

```
