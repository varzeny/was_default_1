import json, os



def get_config():
    try:
        # 환경변수를 건들지 않고도 어느 위치에서든 테스트 할수 있게 만듬
        config_path = os.path.join(
            os.path.dirname( os.path.dirname( os.path.dirname( __file__ ) ) ),
            "config.json"
        )

        with open(config_path,'r') as file:
            return json.load(file)
        
    except Exception as e:
        print( "ERROR : ",e )



CONFIG = get_config()

