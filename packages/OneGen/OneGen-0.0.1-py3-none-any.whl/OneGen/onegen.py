import argparse
#from core.trunk import Trunk
#from utils.sysUtils import load_config
import os


def parse_args():

    description = "OneGen"
    parser = argparse.ArgumentParser(description=description)


    pattern_help ="输入以下命令供OneGen执行: createproject: 创建项目; preprocess: 预处理; train: 训练; test: 测试; eval: 评估; 其中train,test,eval为flow命令"
    parser.add_argument("pattern", help=pattern_help, choices=[
                        "createproject", "preprocess", "train", "test", "eval", "model"], type=str)

    parser.add_argument("-n", "--name", help="项目名称",
                        default=None, metavar="project_name", type=str)

    flow_help = "流处理命令，如果输入pattern的命令是flow命令，加入--flow或-f会继续执行后面的命令，例如：输入 dao train -f，训练结束后会继续执行测试和评估，否则只执行单个命令."
    parser.add_argument("-f", "--flow", action="store_true",
                        help=flow_help, default=False)
    
    parser.add_argument(
        "--local-rank",
        default=os.getenv('LOCAL_RANK'),
        type=int,
    )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    print(args.pattern)
    
    #config=load_config()
    #if args.pattern == "createproject":
        #Trunk.create_project(args.name,config)
    #else:
        #trunk=Trunk(config)

        