import { Component } from '@angular/core';

@Component({
  selector: 'app-lista-tarefa',
  templateUrl: './lista-tarefa.component.html',
  styleUrls: ['./lista-tarefa.component.css']
})
export class ListaTarefaComponent {
  // Define as tarefas iniciais
  tarefa1: Tarefa = new Tarefa("Beber Água");
  tarefa2: Tarefa = new Tarefa("Comer Bolacha");
  tarefa3: Tarefa = new Tarefa("Assistir TV");
  tarefa4: Tarefa = new Tarefa("Deitar na Cama");
  tarefa5: Tarefa = new Tarefa("Estudar");


  tarefas: Array<Tarefa> = [this.tarefa1, this.tarefa2, this.tarefa3, this.tarefa4, this.tarefa5];

  // Função para marcar uma tarefa como concluída
  mudaStatus(tarefa: Tarefa) {
    tarefa.concluido = true;
  }
}


class Tarefa {
  descricao: string = "";
  concluido: boolean = false;

  constructor(descricao: string) {
    this.descricao = descricao;
  }
}