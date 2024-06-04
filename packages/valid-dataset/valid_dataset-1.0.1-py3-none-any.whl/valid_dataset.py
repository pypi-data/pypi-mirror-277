import argparse
import yaml

def main(config_file_path):
    # 从YAML配置文件中读取参数
    with open(config_file_path, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        test = config['TEST']
    print(test)

if __name__ == '__main__':
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Valid dataset')
    parser.add_argument('config_file', type=str, help='path to YAML config file')
    args = parser.parse_args()

    # 执行任务
    main(args.config_file)
