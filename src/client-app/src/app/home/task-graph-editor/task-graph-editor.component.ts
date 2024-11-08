


import { Component, ElementRef, ViewChild, AfterViewInit } from '@angular/core';

interface Node {
  id: string;
  x: number;
  y: number;
  label: string;
  isSelected: boolean;
}

interface Edge {
  id: string;
  source: string;
  target: string;
}

@Component({
  standalone: true,
  imports: [],
  selector: 'app-task-graph-editor',
  templateUrl: './task-graph-editor.component.html',
  styleUrl: './task-graph-editor.component.css'
})
export class TaskGraphEditorComponent implements AfterViewInit  {
  @ViewChild('canvas') canvasRef!: ElementRef<HTMLCanvasElement>;
  private ctx!: CanvasRenderingContext2D;

  width = 800;
  height = 600;
  nodes: Node[] = [];
  edges: Edge[] = [];
  minimalDragAmount = 10;

  private isDragging = false;
  private selectedNode: Node | null = null;
  private dragStartX = 0;
  private dragStartY = 0;
  private nodeRadius = 20;

  ngAfterViewInit() {
    const canvas = this.canvasRef.nativeElement;
    this.ctx = canvas.getContext('2d')!;
    this.drawGraph();
  }

  addNode() {
    const node: Node = {
      id: `node-${this.nodes.length}`,
      x: Math.random() * (this.width - 100) + 50,
      y: Math.random() * (this.height - 100) + 50,
      label: `Node ${this.nodes.length + 1}`,
      isSelected: false
    };
    this.nodes.push(node);
    this.drawGraph();
  }

  addEdge(source: Node, target: Node) {
    const edge: Edge = {
      id: `edge-${this.edges.length}`,
      source: source.id,
      target: target.id,
    }
    this.edges.push(edge)
    this.drawGraph()
  }

  onMouseDown(event: MouseEvent) {
    const rect = this.canvasRef.nativeElement.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    if (this.selectedNode == null) {
      const clicked = this.findNodeAt(x, y);
      if (clicked) {
        this.isDragging = true;
        this.selectedNode = clicked
        this.selectedNode.isSelected = true
        this.dragStartX = clicked.x;
        this.dragStartY = clicked.y;
      }
    } else {
      const source = this.selectedNode
      const target = this.findNodeAt(x, y)


      if (target && target.id != source.id) {
        source.isSelected = false
        this.addEdge(this.selectedNode, target)
        this.selectedNode = null
      }
      else {
        this.selectedNode.isSelected = false
        this.selectedNode = null
      }
    }
    // Check if clicked on a node

    console.log("detected mouse down!")
  }

  onMouseClick(event: MouseEvent) {
  //   const rect = this.canvasRef.nativeElement.getBoundingClientRect();
  //   const x = event.clientX - rect.left;
  //   const y = event.clientY - rect.top;
  //
  //   this.isDragging = false
  //   console.log("detected mouse click!")
  //
  }

  onMouseMove(event: MouseEvent) {

    if (this.isDragging && this.selectedNode) {
      const rect = this.canvasRef.nativeElement.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;

      this.selectedNode.x = x;
      this.selectedNode.y = y;
      console.log(`dragStartX = ${this.dragStartX}`)
      this.drawGraph();
    }
  }

  pointsAreFurtherApartThan(amount: number, point1: { x: number; y: number; }, point2: { x: number; y: number; } ) {
    const dx: number = point1.x - point2.x
    const dy: number = point1.y - point2.y
    console.log(`dx = ${dx}, dy = ${dy}`)
    console.log(`distance2: ${dx * dx + dy * dy}`)
    return dx * dx + dy * dy > amount * amount
  }

  onMouseUp() {

    if (
      this.selectedNode &&
      this.pointsAreFurtherApartThan(this.minimalDragAmount, this.selectedNode, {x: this.dragStartX, y:this.dragStartY})
    ) {
      console.log("mouseup! was dragging so im unselecting all nodes");
      this.selectedNode.isSelected = false
      this.selectedNode = null;
    }
    this.isDragging = false;
    this.drawGraph()
  }

  private findNodeAt(x: number, y: number): Node | null {
    return this.nodes.find(node => {
      const dx = node.x - x;
      const dy = node.y - y;
      return (dx * dx + dy * dy) <= (this.nodeRadius * this.nodeRadius);
    }) || null;
  }

  private drawGraph() {
    if (!this.ctx) return;

    // Clear canvas
    this.ctx.clearRect(0, 0, this.width, this.height);

    // Draw edges
    this.edges.forEach(edge => {
      const source = this.nodes.find(n => n.id === edge.source);
      const target = this.nodes.find(n => n.id === edge.target);
      if (source && target) {
        this.drawEdge(source, target);
      }
    });

    // Draw nodes
    this.nodes.forEach(node => {
      this.drawNode(node);
    });
  }

  private drawNode(node: Node) {
    this.ctx.beginPath();
    this.ctx.lineWidth = 3
    this.ctx.arc(node.x, node.y, this.nodeRadius, 0, Math.PI * 2);
    this.ctx.fillStyle = 'lightblue';
    this.ctx.fill();
    this.ctx.strokeStyle =  node.isSelected ? 'red' : 'blue';
    this.ctx.stroke();

    // Draw label
    this.ctx.fillStyle = 'black';
    this.ctx.textAlign = 'center';
    this.ctx.textBaseline = 'middle';
    this.ctx.fillText(node.label, node.x, node.y);
  }

  private drawEdge(source: Node, target: Node) {
    const headSize = 10;
    const angle = Math.atan2(target.y - source.y, target.x - source.x);

    // Calculate edge endpoints to stop at node boundaries
    const startX = source.x + this.nodeRadius * Math.cos(angle);
    const startY = source.y + this.nodeRadius * Math.sin(angle);
    const endX = target.x - (this.nodeRadius + headSize) * Math.cos(angle);
    const endY = target.y - (this.nodeRadius + headSize) * Math.sin(angle);

    this.ctx.beginPath();
    this.ctx.moveTo(startX, startY);
    this.ctx.lineTo(endX, endY);
    this.ctx.strokeStyle = 'black';
    this.ctx.stroke();

    // Draw arrow head
    this.ctx.beginPath();
    this.ctx.moveTo(endX, endY);
    this.ctx.lineTo(
      endX - headSize * Math.cos(angle - Math.PI / 6),
      endY - headSize * Math.sin(angle - Math.PI / 6)
    );
    this.ctx.lineTo(
      endX - headSize * Math.cos(angle + Math.PI / 6),
      endY - headSize * Math.sin(angle + Math.PI / 6)
    );
    this.ctx.closePath();
    this.ctx.fillStyle = 'black';
    this.ctx.fill();
  }

  clearCanvas() {
    this.nodes = [];
    this.edges = [];
    this.drawGraph();
  }
}
