# Copyright 2023 ENID
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""File defining the LucidRnn Detection Engine"""
from .lucid_mlp import LucidMlp, tf


class LucidRnn(LucidMlp):
    """Detection Engine composed of:
    - Lucid traffic processing mechanism
    - RNN (LSTM) as model architecture
    - Same training parameters and combination defined in LucidCnn
    """

    @classmethod
    def _get_arch(
            cls, packets_per_session: int = None, features: int = None,
            max_packets_per_session: int = None, max_features: int = None,
            kernels: int = 64, dropout: float = 0.2,
            learning_rate: float = 0.001, **kwargs):
        if max_packets_per_session:
            packets_per_session = max_packets_per_session
        if max_features:
            features = max_features
        model = tf.keras.models.Sequential([
            tf.keras.layers.LSTM(kernels, input_shape=(
                packets_per_session, features), name="TARGET"),
            tf.keras.layers.Dropout(dropout, name="Dropout"),
            tf.keras.layers.Activation(
                tf.keras.activations.relu, name="ReLu"),
            tf.keras.layers.Dense(1, name='FinalDense'),
            tf.keras.layers.Activation(
                tf.keras.activations.sigmoid, name="Sigmoid")
        ], name=cls.model_name(packets_per_session=packets_per_session, features=features))

        if learning_rate:
            model.compile(loss=tf.keras.metrics.binary_crossentropy,
                          optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                          metrics=["accuracy"])

        return model
