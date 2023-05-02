from django.db import models


class Status(models.Model):
    descricao_status = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao_status


class Editora(models.Model):
    nome_editora = models.CharField(max_length=200)
    local_editora = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_editora


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=400, blank=True)
    autor = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, blank=True)
    ano = models.IntegerField(blank=True, null=True)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
