class BufferController:

    def search_buffer(self, m):
        arquivo = open('../buffer/buffer.txt', 'r')
        m_string = "[" + " ".join(str(x) for x in m) + "]"
        for linha in arquivo:
            aux = linha[0:61]
            if m_string == aux:
                aux2 = linha[62:-1]
                # print('Retornando Merito Encontrado')
                return float(aux2)
        # print('Merito não encontrado')
        arquivo.close()
        return None

    def save_buffer(self, m, merito):
        arquivo = open('../buffer/buffer.txt', 'r') 
        conteudo = arquivo.readlines()
        
        texto = '[' + ' '.join(str(x) for x in m) + '] ' + repr(merito) + '\n'
        # print('Salvando Novo Mérito')
        conteudo.append(texto)   
        
        arquivo = open('../buffer/buffer.txt', 'w')
        arquivo.writelines(conteudo)   

        arquivo.close
