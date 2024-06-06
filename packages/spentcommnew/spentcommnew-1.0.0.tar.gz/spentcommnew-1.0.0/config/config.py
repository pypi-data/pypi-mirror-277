from omegaconf import OmegaConf

# Define the path to your configuration file
config_path = (
    "/home/jupyter/code/sapient/knowledge-powerhouse-pocs/kph/src/config/config.yaml"
)

# Load the configuration file from the specified path
config = OmegaConf.load(config_path)
