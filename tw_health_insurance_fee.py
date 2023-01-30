def get_insurance_amount_level(salary):
    salary_levels = [0,25250,26400,27600,28800,30300,31800,33300,34800,36300,38200,40100,42000,43900,45800,48200,50600,53000,55400,57800,60800,63800,66800,69800,72800,76500,80200,83900,87600,92100,96600,101100,105600,110100,115500,120900,126300,131700,137100,142500,147900,150000,156400,162800,169200,175600,182000,189500,197000,204500,212000,219500]
    left, right = 0, len(salary_levels) - 1
    while left <= right:
        mid = (left + right) // 2
        if salary < salary_levels[mid]:
            right = mid - 1
        elif salary > salary_levels[mid]:
            left = mid + 1
        else:
            return mid
    return left-1

def get_coverage_amount(insurance_amount):
    coverage_data = {
    "0": {
        "level": "error",
        "salary": "error",
        "Self": "error",
        "Self_with_1_family": "error",
        "Self_with_2_family": "error",
        "Self_with_3_family": "error",
        "Company": "error",
        "Government": "error"
    },
    "1": {
        "level": "1",
        "salary": "25250",
        "Self": "392",
        "Self_with_1_family": "784",
        "Self_with_2_family": "1176",
        "Self_with_3_family": "1568",
        "Company": "1238",
        "Government": "206"
    },
    "2": {
        "level": "2",
        "salary": "26400",
        "Self": "409",
        "Self_with_1_family": "818",
        "Self_with_2_family": "1227",
        "Self_with_3_family": "1636",
        "Company": "1294",
        "Government": "216"
    },
    "3":{
    	"level": "3",
    	"salary": "27600",
    	"Self": "428",
    	"Self_with_1_family": "856",
    	"Self_with_2_family": "1284",
    	"Self_with_3_family": "1712",
    	"Company": "1353",
    	"Government": "225"
    },
    "4":{
    	"level": "4",
    	"salary": "28800",
    	"Self": "447",
    	"Self_with_1_family": "894",
    	"Self_with_2_family": "1341",
    	"Self_with_3_family": "1788",
    	"Company": "1412",
    	"Government": "235"
    },
    "5":{
    	"level": "5",
    	"salary": "30300",
    	"Self": "470",
    	"Self_with_1_family": "940",
    	"Self_with_2_family": "1410",
    	"Self_with_3_family": "1880",
    	"Company": "1485",
    	"Government": "248"
    },
    "6":{
    	"level": "6",
    	"salary": "31800",
    	"Self": "493",
    	"Self_with_1_family": "986",
    	"Self_with_2_family": "1479",
    	"Self_with_3_family": "1972",
    	"Company": "1559",
    	"Government": "260"
    },
    "7":{
    	"level": "7",
    	"salary": "33300",
    	"Self": "516",
    	"Self_with_1_family": "1032",
    	"Self_with_2_family": "1548",
    	"Self_with_3_family": "2064",
    	"Company": "1632",
    	"Government": "272"
    },
    "8":{
    	"level": "8",
    	"salary": "34800",
    	"Self": "540",
    	"Self_with_1_family": "1080",
    	"Self_with_2_family": "1620",
    	"Self_with_3_family": "2160",
    	"Company": "1706",
    	"Government": "284"
    },
    "9":{
    	"level": "9",
    	"salary": "36300",
    	"Self": "563",
    	"Self_with_1_family": "1126",
    	"Self_with_2_family": "1689",
    	"Self_with_3_family": "2252",
    	"Company": "1779",
    	"Government": "297"
    },
    "10":{
	    "level": "10",
	    "salary": "38200",
	    "Self": "592",
	    "Self_with_1_family": "1184",
	    "Self_with_2_family": "1776",
	    "Self_with_3_family": "2368",
	    "Company": "1872",
	    "Government": "312"
    },
    "11":{
	    "level": "11",
	    "salary": "40100",
	    "Self": "622",
	    "Self_with_1_family": "1244",
	    "Self_with_2_family": "1866",
	    "Self_with_3_family": "2488",
	    "Company": "1965",
	    "Government": "328"
    },
    "12":{
	    "level": "12",
	    "salary": "42000",
	    "Self": "651",
	    "Self_with_1_family": "1302",
	    "Self_with_2_family": "1953",
	    "Self_with_3_family": "2604",
	    "Company": "2058",
	    "Government": "343"
    },
    "13":{
	    "level": "13",
	    "salary": "43900",
	    "Self": "681",
	    "Self_with_1_family": "1362",
	    "Self_with_2_family": "2043",
	    "Self_with_3_family": "2724",
	    "Company": "2152",
	    "Government": "359"
    },
    "14":{
	    "level": "14",
	    "salary": "45800",
	    "Self": "710",
	    "Self_with_1_family": "1420",
	    "Self_with_2_family": "2130",
	    "Self_with_3_family": "2840",
	    "Company": "2245",
	    "Government": "374"
    },
    "15":{
	    "level": "15",
	    "salary": "48200",
	    "Self": "748",
	    "Self_with_1_family": "1496",
	    "Self_with_2_family": "2244",
	    "Self_with_3_family": "2992",
	    "Company": "2362",
	    "Government": "394"
    },
    "16":{
	    "level": "16",
	    "salary": "50600",
	    "Self": "785",
	    "Self_with_1_family": "1570",
	    "Self_with_2_family": "2355",
	    "Self_with_3_family": "3140",
	    "Company": "2480",
	    "Government": "413"
    },
    "17":{
	    "level": "17",
	    "salary": "53000",
	    "Self": "822",
	    "Self_with_1_family": "1644",
	    "Self_with_2_family": "2466",
	    "Self_with_3_family": "3288",
	    "Company": "2598",
	    "Government": "433"
    },
    "18":{
	    "level": "18",
	    "salary": "55400",
	    "Self": "859",
	    "Self_with_1_family": "1718",
	    "Self_with_2_family": "2577",
	    "Self_with_3_family": "3436",
	    "Company": "2715",
	    "Government": "453"
    },
    "19":{
	    "level": "19",
	    "salary": "57800",
	    "Self": "896",
	    "Self_with_1_family": "1792",
	    "Self_with_2_family": "2688",
	    "Self_with_3_family": "3584",
	    "Company": "2833",
	    "Government": "472"
    },
    "20":{
	    "level": "20",
	    "salary": "60800",
	    "Self": "943",
	    "Self_with_1_family": "1886",
	    "Self_with_2_family": "2829",
	    "Self_with_3_family": "3772",
	    "Company": "2980",
	    "Government": "497"
    },
    "21":{
	    "level": "21",
	    "salary": "63800",
	    "Self": "990",
	    "Self_with_1_family": "1980",
	    "Self_with_2_family": "2970",
	    "Self_with_3_family": "3960",
	    "Company": "3127",
	    "Government": "521"
    },
    "22":{
	    "level": "22",
	    "salary": "66800",
	    "Self": "1036",
	    "Self_with_1_family": "2072",
	    "Self_with_2_family": "3108",
	    "Self_with_3_family": "4144",
	    "Company": "3274",
	    "Government": "546"
    },
    "23":{
	    "level": "23",
	    "salary": "69800",
	    "Self": "1083",
	    "Self_with_1_family": "2166",
	    "Self_with_2_family": "3249",
	    "Self_with_3_family": "4332",
	    "Company": "3421",
	    "Government": "570"
    },
    "24":{
	    "level": "24",
	    "salary": "72800",
	    "Self": "1129",
	    "Self_with_1_family": "2258",
	    "Self_with_2_family": "3387",
	    "Self_with_3_family": "4516",
	    "Company": "3568",
	    "Government": "595"
    },
    "25":{
	    "level": "25",
	    "salary": "76500",
	    "Self": "1187",
	    "Self_with_1_family": "2374",
	    "Self_with_2_family": "3561",
	    "Self_with_3_family": "4748",
	    "Company": "3749",
	    "Government": "625"
    },
    "26":{
	    "level": "26",
	    "salary": "80200",
	    "Self": "1244",
	    "Self_with_1_family": "2488",
	    "Self_with_2_family": "3732",
	    "Self_with_3_family": "4976",
	    "Company": "3931",
	    "Government": "655"
    },
    "27":{
	    "level": "27",
	    "salary": "83900",
	    "Self": "1301",
	    "Self_with_1_family": "2602",
	    "Self_with_2_family": "3903",
	    "Self_with_3_family": "5204",
	    "Company": "4112",
	    "Government": "685"
    },
    "28":{
	    "level": "28",
	    "salary": "87600",
	    "Self": "1359",
	    "Self_with_1_family": "2718",
	    "Self_with_2_family": "4077",
	    "Self_with_3_family": "5436",
	    "Company": "4293",
	    "Government": "716"
    },
    "29":{
	    "level": "29",
	    "salary": "92100",
	    "Self": "1428",
	    "Self_with_1_family": "2856",
	    "Self_with_2_family": "4284",
	    "Self_with_3_family": "5712",
	    "Company": "4514",
	    "Government": "752"
    },
    "30":{
	    "level": "30",
	    "salary": "96600",
	    "Self": "1498",
	    "Self_with_1_family": "2996",
	    "Self_with_2_family": "4494",
	    "Self_with_3_family": "5992",
	    "Company": "4735",
	    "Government": "789"
    },
    "31":{
	    "level": "31",
	    "salary": "101100",
	    "Self": "1568",
	    "Self_with_1_family": "3136",
	    "Self_with_2_family": "4704",
	    "Self_with_3_family": "6272",
	    "Company": "4955",
	    "Government": "826"
    },
    "32":{
	    "level": "32",
	    "salary": "105600",
	    "Self": "1638",
	    "Self_with_1_family": "3276",
	    "Self_with_2_family": "4914",
	    "Self_with_3_family": "6552",
	    "Company": "5176",
	    "Government": "863"
    },
    "33":{
	    "level": "33",
	    "salary": "110100",
	    "Self": "1708",
	    "Self_with_1_family": "3416",
	    "Self_with_2_family": "5124",
	    "Self_with_3_family": "6832",
	    "Company": "5396",
	    "Government": "899"
    },
    "34":{
	    "level": "34",
	    "salary": "115500",
	    "Self": "1791",
	    "Self_with_1_family": "3582",
	    "Self_with_2_family": "5373",
	    "Self_with_3_family": "7164",
	    "Company": "5661",
	    "Government": "943"
    },
    "35":{
	    "level": "35",
	    "salary": "120900",
	    "Self": "1875",
	    "Self_with_1_family": "3750",
	    "Self_with_2_family": "5625",
	    "Self_with_3_family": "7500",
	    "Company": "5926",
	    "Government": "988"
    },
    "36":{
	    "level": "36",
	    "salary": "126300",
	    "Self": "1959",
	    "Self_with_1_family": "3918",
	    "Self_with_2_family": "5877",
	    "Self_with_3_family": "7836",
	    "Company": "6190",
	    "Government": "1032"
    },
    "37":{
	    "level": "37",
	    "salary": "131700",
	    "Self": "2043",
	    "Self_with_1_family": "4086",
	    "Self_with_2_family": "6129",
	    "Self_with_3_family": "8172",
	    "Company": "6455",
	    "Government": "1076"
    },
    "38":{
	    "level": "38",
	    "salary": "137100",
	    "Self": "2126",
	    "Self_with_1_family": "4252",
	    "Self_with_2_family": "6378",
	    "Self_with_3_family": "8504",
	    "Company": "6719",
	    "Government": "1120"
    },
    "39":{
	    "level": "39",
	    "salary": "142500",
	    "Self": "2210",
	    "Self_with_1_family": "4420",
	    "Self_with_2_family": "6630",
	    "Self_with_3_family": "8840",
	    "Company": "6984",
	    "Government": "1164"
    },
    "40":{
	    "level": "40",
	    "salary": "147900",
	    "Self": "2294",
	    "Self_with_1_family": "4588",
	    "Self_with_2_family": "6882",
	    "Self_with_3_family": "9176",
	    "Company": "7249",
	    "Government": "1208"
    },
    "41":{
	    "level": "41",
	    "salary": "150000",
	    "Self": "2327",
	    "Self_with_1_family": "4654",
	    "Self_with_2_family": "6981",
	    "Self_with_3_family": "9308",
	    "Company": "7352",
	    "Government": "1225"
    },
    "42":{
	    "level": "42",
	    "salary": "156400",
	    "Self": "2426",
	    "Self_with_1_family": "4852",
	    "Self_with_2_family": "7278",
	    "Self_with_3_family": "9704",
	    "Company": "7665",
	    "Government": "1278"
    },
    "43":{
	    "level": "43",
	    "salary": "162800",
	    "Self": "2525",
	    "Self_with_1_family": "5050",
	    "Self_with_2_family": "7575",
	    "Self_with_3_family": "10100",
	    "Company": "7979",
	    "Government": "1330"
    },
    "44":{
	    "level": "44",
	    "salary": "169200",
	    "Self": "2624",
	    "Self_with_1_family": "5248",
	    "Self_with_2_family": "7872",
	    "Self_with_3_family": "10496",
	    "Company": "8293",
	    "Government": "1382"
    },
    "45":{
	    "level": "45",
	    "salary": "175600",
	    "Self": "2724",
	    "Self_with_1_family": "5448",
	    "Self_with_2_family": "8172",
	    "Self_with_3_family": "10896",
	    "Company": "8606",
	    "Government": "1434"
    },
    "46":{
	    "level": "46",
	    "salary": "182000",
	    "Self": "2823",
	    "Self_with_1_family": "5646",
	    "Self_with_2_family": "8469",
	    "Self_with_3_family": "11292",
	    "Company": "8920",
	    "Government": "1487"
    },
    "47":{
	    "level": "47",
	    "salary": "189500",
	    "Self": "2939",
	    "Self_with_1_family": "5878",
	    "Self_with_2_family": "8817",
	    "Self_with_3_family": "11756",
	    "Company": "9288",
	    "Government": "1548"
    },
    "48":{
	    "level": "48",
	    "salary": "197000",
	    "Self": "3055",
	    "Self_with_1_family": "6110",
	    "Self_with_2_family": "9165",
	    "Self_with_3_family": "12220",
	    "Company": "9655",
	    "Government": "1609"
    },
    "49":{
	    "level": "49",
	    "salary": "204500",
	    "Self": "3172",
	    "Self_with_1_family": "6344",
	    "Self_with_2_family": "9516",
	    "Self_with_3_family": "12688",
	    "Company": "10023",
	    "Government": "1670"
    },
    "50":{
	    "level": "50",
	    "salary": "212000",
	    "Self": "3288",
	    "Self_with_1_family": "6576",
	    "Self_with_2_family": "9864",
	    "Self_with_3_family": "13152",
	    "Company": "10390",
	    "Government": "1732"
    },
    "51":{
	    "level": "51",
	    "salary": "219500",
	    "Self": "3404",
	    "Self_with_1_family": "6808",
	    "Self_with_2_family": "10212",
	    "Self_with_3_family": "13616",
	    "Company": "10758",
	    "Government": "1793"
    }
    }
    return coverage_data.get(insurance_amount, {})
salary = contract.wage
level = str(get_insurance_amount_level(salary))
dictionary = get_coverage_amount(level)
result = dictionary['Self']
 
