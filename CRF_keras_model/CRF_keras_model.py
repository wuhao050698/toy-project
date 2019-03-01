# -- codingutf-8 --

from keras.layers import Layer
import keras.backend as K


class CRF(Layer)
    ��Kerasʵ��CRF��
    CRF�㱾������һ����ѵ��������loss����㣬���CRF��ֻ����ѵ��ģ�ͣ�
    ��Ԥ������Ҫ���⽨��ģ�͡�
    
    def __init__(self, ignore_last_label=False, kwargs)
        ignore_last_label������Ҫ��Ҫ�������һ����ǩ����mask��Ч��
        
        self.ignore_last_label = 1 if ignore_last_label else 0
        super(CRF, self).__init__(kwargs)
    def build(self, input_shape)
        self.num_labels = input_shape[-1] - self.ignore_last_label
        self.trans = self.add_weight(name='crf_trans',
                                     shape=(self.num_labels, self.num_labels),
                                     initializer='glorot_uniform',
                                     trainable=True)
    def log_norm_step(self, inputs, states)
        �ݹ�����һ������
        Ҫ�㣺1���ݹ���㣻2����logsumexp���������
        ���ɣ�ͨ��expand_dims������������
        
        states = K.expand_dims(states[0], 2) # (batch_size, output_dim, 1)
        trans = K.expand_dims(self.trans, 0) # (1, output_dim, output_dim)
        output = K.logsumexp(states+trans, 1) # (batch_size, output_dim)
        return output+inputs, [output+inputs]
    def path_score(self, inputs, labels)
        ����Ŀ��·������Ը��ʣ���û�й�һ����
        Ҫ�㣺���ǩ�÷֣�����ת�Ƹ��ʵ÷֡�
        ���ɣ��á�Ԥ�⡱��ˡ�Ŀ�ꡱ�ķ�����ȡ��Ŀ��·���ĵ÷֡�
        
        point_score = K.sum(K.sum(inputslabels, 2), 1, keepdims=True) # ���ǩ�÷�
        labels1 = K.expand_dims(labels[, -1], 3)
        labels2 = K.expand_dims(labels[, 1], 2)
        labels = labels1  labels2 # ������λlabels�������ת�ƾ����г�ȡĿ��ת�Ƶ÷�
        trans = K.expand_dims(K.expand_dims(self.trans, 0), 0)
        trans_score = K.sum(K.sum(translabels, [2,3]), 1, keepdims=True)
        return point_score+trans_score # �����ֵ÷�֮��
    def call(self, inputs) # CRF�����ı��������ֻ��һ��loss
        return inputs
    def loss(self, y_true, y_pred) # Ŀ��y_pred��Ҫ��one hot��ʽ
        mask = 1-y_true[,1,-1] if self.ignore_last_label else None
        y_true,y_pred = y_true[,,self.num_labels],y_pred[,,self.num_labels]
        init_states = [y_pred[,0]] # ��ʼ״̬
        log_norm,_,_ = K.rnn(self.log_norm_step, y_pred[,1], init_states, mask=mask) # ����Z������������
        log_norm = K.logsumexp(log_norm, 1, keepdims=True) # ����Z��������
        path_score = self.path_score(y_pred, y_true) # ������ӣ�������
        return log_norm - path_score # ��log(���ӷ�ĸ)
    def accuracy(self, y_true, y_pred) # ѵ����������ʾ��֡׼ȷ�ʵĺ������ų���mask��Ӱ��
        mask = 1-y_true[,,-1] if self.ignore_last_label else None
        y_true,y_pred = y_true[,,self.num_labels],y_pred[,,self.num_labels]
        isequal = K.equal(K.argmax(y_true, 2), K.argmax(y_pred, 2))
        isequal = K.cast(isequal, 'float32')
        if mask == None
            return K.mean(isequal)
        else
            return K.sum(isequalmask)  K.sum(mask)