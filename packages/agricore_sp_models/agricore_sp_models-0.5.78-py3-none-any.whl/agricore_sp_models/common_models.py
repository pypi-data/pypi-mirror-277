from re import S
from pydantic import BaseModel
from typing import Optional, List
from enum import IntEnum
from agricore_sp_models import CaseInsensitiveModel

class OrganicProductionType(IntEnum):
    Conventional = 0
    Organic = 1
    Undetermined = 2
    
class FADNProductJsonDTO(CaseInsensitiveModel):
    fadnIdentifier: str
    description: str
    productType: str
    arable: bool
    # The representativeness of the FADN product in the product group. Item representativeness should be calculated
    # as the representativeness of the FADN product divided by the sum of the representativeness of all FADN products in the product group.
    # For its calculation, remember than whe obtaining data from the sample, the weight of such farm in the population should be taken into account
    representativenessOcurrence: Optional[float] = None
    # In hectars
    representativenessArea: Optional[float] = None
    # In €
    representativenessValue: Optional[float] = None
    
class PolicyJsonDTO(CaseInsensitiveModel):
    populationId: int
    policyIdentifier: str
    isCoupled: bool
    policyDescription: str
    economicCompensation: float
    modelLabel: Optional[str]
    startYearNumber: int
    endYearNumber: int

    
class PolicyGroupRelationJsonDTO(CaseInsensitiveModel):
    populationId: int
    policyIdentifier: str
    productGroupName: str
    economicCompensation: float
    
class ProductGroupJsonDTO(CaseInsensitiveModel):
    name: str
    productType: str
    originalNameDatasource: str
    productsIncludedInOriginalDataset: str
    modelSpecificCategories: List[str]
    organic: OrganicProductionType
    fadnProducts: List[FADNProductJsonDTO]
    
class LandRentJsonDTO(CaseInsensitiveModel):
    yearNumber: int
    originFarmCode: str
    destinationFarmCode: str
    # Total Rent Price [€]
    rentValue: float
    # Total Rent Area [ha]
    rentArea: float
    
class LandRentDTO(CaseInsensitiveModel):
    yearId: int
    originFarmId: int
    destinationFarmId: int
    # Total Rent Price [€]
    rentValue: float
    # Total Rent Area [ha]
    rentArea: float