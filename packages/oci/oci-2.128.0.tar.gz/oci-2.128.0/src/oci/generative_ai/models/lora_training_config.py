# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130

from .training_config import TrainingConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoraTrainingConfig(TrainingConfig):
    """
    The Lora training method hyperparameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LoraTrainingConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai.models.LoraTrainingConfig.training_config_type` attribute
        of this class is ``LORA_TRAINING_CONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param training_config_type:
            The value to assign to the training_config_type property of this LoraTrainingConfig.
            Allowed values for this property are: "TFEW_TRAINING_CONFIG", "VANILLA_TRAINING_CONFIG", "LORA_TRAINING_CONFIG"
        :type training_config_type: str

        :param total_training_epochs:
            The value to assign to the total_training_epochs property of this LoraTrainingConfig.
        :type total_training_epochs: int

        :param learning_rate:
            The value to assign to the learning_rate property of this LoraTrainingConfig.
        :type learning_rate: float

        :param training_batch_size:
            The value to assign to the training_batch_size property of this LoraTrainingConfig.
        :type training_batch_size: int

        :param early_stopping_patience:
            The value to assign to the early_stopping_patience property of this LoraTrainingConfig.
        :type early_stopping_patience: int

        :param early_stopping_threshold:
            The value to assign to the early_stopping_threshold property of this LoraTrainingConfig.
        :type early_stopping_threshold: float

        :param log_model_metrics_interval_in_steps:
            The value to assign to the log_model_metrics_interval_in_steps property of this LoraTrainingConfig.
        :type log_model_metrics_interval_in_steps: int

        :param lora_r:
            The value to assign to the lora_r property of this LoraTrainingConfig.
        :type lora_r: int

        :param lora_alpha:
            The value to assign to the lora_alpha property of this LoraTrainingConfig.
        :type lora_alpha: int

        :param lora_dropout:
            The value to assign to the lora_dropout property of this LoraTrainingConfig.
        :type lora_dropout: float

        """
        self.swagger_types = {
            'training_config_type': 'str',
            'total_training_epochs': 'int',
            'learning_rate': 'float',
            'training_batch_size': 'int',
            'early_stopping_patience': 'int',
            'early_stopping_threshold': 'float',
            'log_model_metrics_interval_in_steps': 'int',
            'lora_r': 'int',
            'lora_alpha': 'int',
            'lora_dropout': 'float'
        }

        self.attribute_map = {
            'training_config_type': 'trainingConfigType',
            'total_training_epochs': 'totalTrainingEpochs',
            'learning_rate': 'learningRate',
            'training_batch_size': 'trainingBatchSize',
            'early_stopping_patience': 'earlyStoppingPatience',
            'early_stopping_threshold': 'earlyStoppingThreshold',
            'log_model_metrics_interval_in_steps': 'logModelMetricsIntervalInSteps',
            'lora_r': 'loraR',
            'lora_alpha': 'loraAlpha',
            'lora_dropout': 'loraDropout'
        }

        self._training_config_type = None
        self._total_training_epochs = None
        self._learning_rate = None
        self._training_batch_size = None
        self._early_stopping_patience = None
        self._early_stopping_threshold = None
        self._log_model_metrics_interval_in_steps = None
        self._lora_r = None
        self._lora_alpha = None
        self._lora_dropout = None
        self._training_config_type = 'LORA_TRAINING_CONFIG'

    @property
    def lora_r(self):
        """
        Gets the lora_r of this LoraTrainingConfig.
        This parameter represents the LoRA rank of the update matrices.


        :return: The lora_r of this LoraTrainingConfig.
        :rtype: int
        """
        return self._lora_r

    @lora_r.setter
    def lora_r(self, lora_r):
        """
        Sets the lora_r of this LoraTrainingConfig.
        This parameter represents the LoRA rank of the update matrices.


        :param lora_r: The lora_r of this LoraTrainingConfig.
        :type: int
        """
        self._lora_r = lora_r

    @property
    def lora_alpha(self):
        """
        Gets the lora_alpha of this LoraTrainingConfig.
        This parameter represents the scaling factor for the weight matrices in LoRA.


        :return: The lora_alpha of this LoraTrainingConfig.
        :rtype: int
        """
        return self._lora_alpha

    @lora_alpha.setter
    def lora_alpha(self, lora_alpha):
        """
        Sets the lora_alpha of this LoraTrainingConfig.
        This parameter represents the scaling factor for the weight matrices in LoRA.


        :param lora_alpha: The lora_alpha of this LoraTrainingConfig.
        :type: int
        """
        self._lora_alpha = lora_alpha

    @property
    def lora_dropout(self):
        """
        Gets the lora_dropout of this LoraTrainingConfig.
        This parameter indicates the dropout probability for LoRA layers.


        :return: The lora_dropout of this LoraTrainingConfig.
        :rtype: float
        """
        return self._lora_dropout

    @lora_dropout.setter
    def lora_dropout(self, lora_dropout):
        """
        Sets the lora_dropout of this LoraTrainingConfig.
        This parameter indicates the dropout probability for LoRA layers.


        :param lora_dropout: The lora_dropout of this LoraTrainingConfig.
        :type: float
        """
        self._lora_dropout = lora_dropout

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
