''' 딕셔너리를 이용해서 txt 파일에 있는 지하철 역들을 key로 하고, 그 노드를 value로 하는 그래프 생성 '''

class StationNode:
    """간단한 지하철 역 노드 클래스"""
    def __init__(self, station_name):
        self.station_name = station_name

def create_station_nodes(input_file):
    """input_file에서 데이터를 읽어 와서 지하철 그래프 노드들을 리턴하는 함수"""
    stations = {}  # 지하철 역 노드들을 담을 딕셔너리

    # 파라미터로 받은 input_file 파일을 연다
    with open(input_file) as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            subway_line = line.strip().split("-")  # 앞 뒤 띄어쓰기를 없애고 "-"를 기준점으로 데이터를 나눈다

            for name in subway_line:
                station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기

                stations[station_name] = StationNode(station_name)

    return stations

stations = create_station_nodes("./stations.txt")  # stations.txt 파일로 그래프 노드들을 만든다

# stations에 저장한 역들 이름 출력 (체점을 위해 역 이름 순서대로 출력)
for station in sorted(stations.keys()):
    print(stations[station].station_name)
