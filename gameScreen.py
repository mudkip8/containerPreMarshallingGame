import copy

import pygame


class GameScreen:
    def __init__(self, screen: pygame.Surface):
        self.colors = [(242, 242, 242), 'red', 'orange', 'light blue', 'light green', 'pink', 'yellow', 'aqua', 'orchid'
                                                                                                                'fuchsia',
                       'light salmon']
        self.row_max_heights = [4, 5, 5, 5, 5, 5]
        self.initial_state = [[0, 0, 0, 0, -1],
                              [1, 1, 1, 2, 2],
                              [3, 3, 4, 3, 1],
                              [6, 6, 5, 5, 5],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0]]  # 0 means unoccupied position
        self.slot_layout = copy.deepcopy(self.initial_state)
        self.cntr_width = 100
        self.cntr_height = 80
        self.spacing = 30
        self.slot_start_x = 220
        self.slot_start_y = 140
        self.row_boundaries = [self.slot_start_x + (self.cntr_width + self.spacing) * num for num in range(6)]
        self.move_count = 0
        self.font = pygame.font.Font(None, 30)
        self.rule_text = self.font.render("", True, 'white')
        self.row_boxes = []
        self.is_origin_selected = False
        self.origin_row = None
        self.hover_rect = None

    def check_legal_move(self, origin, dest):
        if len([cntr for cntr in self.slot_layout[origin] if cntr > 0]) == 0:
            return False, f"Row {origin + 1} Is Empty!"
        if len([cntr for cntr in self.slot_layout[dest] if cntr > 0]) >= self.row_max_heights[dest]:
            return False, f"Row {dest + 1} Is Full!"
        return True, ""

    def make_move(self, origin, dest):
        dest_level = self.slot_layout[dest].index(0)
        origin_len = len([cntr for cntr in self.slot_layout[origin] if cntr > 0])
        origin_cntr = self.slot_layout[origin][origin_len - 1]
        self.slot_layout[origin][origin_len - 1] = 0
        self.slot_layout[dest][dest_level] = origin_cntr

    def handle_event(self, event: pygame.event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            rule_error_message = ""
            for i, rect in enumerate(self.row_boxes):
                if rect.collidepoint(event.pos):
                    if not self.is_origin_selected:
                        self.origin_row = i
                        self.is_origin_selected = True
                    else:
                        is_legal, rule_error_message = self.check_legal_move(self.origin_row, i)
                        if is_legal:
                            self.make_move(self.origin_row, i)
                            self.move_count += 1
                        self.origin_row = None
                        self.is_origin_selected = False
            self.rule_text = self.font.render(rule_error_message, True, 'red')
        mouse_pos = pygame.mouse.get_pos()
        for i, rect in enumerate(self.row_boxes):
            if rect.collidepoint(mouse_pos):
                if rect != self.origin_row:
                    self.hover_rect = pygame.Rect(self.row_boundaries[i] - 5, self.slot_start_y - 5,
                                                  self.cntr_width + 10, self.cntr_height * 5 + 10)
                    return None
        self.hover_rect = None
        return None

    def draw(self, screen: pygame.Surface):
        screen.fill('white')
        row_boxes = []
        floor_rect = pygame.Rect(0, self.slot_start_y + 5 * self.cntr_height - 2, screen.get_width(), 7)
        pygame.draw.rect(screen, 'black', floor_rect)
        for row_num, row in enumerate(self.slot_layout):
            row_rect = pygame.Rect(self.row_boundaries[row_num], self.slot_start_y, self.cntr_width,
                                   5 * self.cntr_height)
            row_boxes.append(row_rect)
            for level, cntr in enumerate(row):
                if cntr < 0:
                    continue
                # Draw 2 rectangles. 1 specifies avail space, 1 specifiies lying containers.
                cntr_rect = pygame.Rect(self.row_boundaries[row_num],
                                        self.slot_start_y + self.cntr_height * (4 - level),
                                        self.cntr_width,
                                        self.cntr_height)
                pygame.draw.rect(screen, self.colors[cntr], cntr_rect, 0)
                pygame.draw.rect(screen, 'black', cntr_rect, 2)
                if cntr > 0:
                    cntr_text = self.font.render(str(cntr), True, 'black')
                    screen.blit(cntr_text, (cntr_rect.centerx - 5, cntr_rect.centery - 10))
            row_label_text = self.font.render(f"Row {row_num + 1}", True, 'black')
            row_label_rect = row_label_text.get_rect()
            row_label_rect.centerx = self.row_boundaries[row_num] + self.cntr_width // 2
            row_label_rect.centery = self.slot_start_y + 5 * self.cntr_height + self.spacing
            screen.blit(row_label_text, row_label_rect)
            if self.hover_rect:
                pygame.draw.rect(screen, 'dark blue', self.hover_rect, 5)
            if self.is_origin_selected:
                select_rect = pygame.Rect(self.row_boundaries[self.origin_row] - 5, self.slot_start_y - 5, self.cntr_width + 10,
                                          self.cntr_height * 5 + 10)
                pygame.draw.rect(screen, 'green', select_rect, 5)
            text_width = self.rule_text.get_width()
            screen.blit(self.rule_text, ((screen.get_width() - text_width) // 2, self.slot_start_y + 6 * self.cntr_height))
            move_counter_text = self.font.render(f"Number of moves: {self.move_count}", True, 'black')
            screen.blit(move_counter_text, (10, 10))

        self.row_boxes = row_boxes
