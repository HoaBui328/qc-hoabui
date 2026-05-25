# Question Backlog

> Generated: 2026-05-15
> Source files: UC87_tra-cuu-du-an-keu-goi-dau-tu_srs_20260515_v1.3.md

---

## Answered Questions

| ID | Priority | Ref | Question | Answer | Answered By | Date | Status |
|----|----------|-----|----------|--------|-------------|------|--------|
| QA-001 | H | UC87 §2.1 | "NĐT tự đề xuất dự án" có thuộc scope UC87 không? | Không — bỏ khỏi UC87. Hub chỉ còn 2 chức năng (Bổ sung thông tin + Danh sách đề xuất) | BA (HieuLuu) | 2026-05-15 | Answered |
| QA-002 | H | UC87 §2.3 | NĐT chưa bổ sung thông tin → vào Danh sách đề xuất → hiển thị gì? | Danh sách rỗng + thông báo gợi ý "Vui lòng bổ sung thông tin để nhận gợi ý dự án phù hợp" | BA (HieuLuu) | 2026-05-15 | Answered |
| QA-003 | M | UC87 §2.3 | NĐT có bị giới hạn số dự án đăng ký quan tâm không? | Không giới hạn | BA (HieuLuu) | 2026-05-15 | Answered |
| QA-004 | H | UC87 §2.2 | Matching diễn ra realtime hay batch? | Realtime — gọi API ngay, chờ kết quả | BA (HieuLuu) | 2026-05-15 | Answered |
| QA-005 | M | UC87 §2.4 | Có field nào bị ẩn cho đến khi NĐT đăng ký quan tâm? | Không — hiển thị toàn bộ chi tiết cho mọi NĐT đã đăng nhập | BA (HieuLuu) | 2026-05-15 | Answered |
| QA-006 | H | UC87 §2.2 | NĐT quay lại form bổ sung thông tin — form trống hay giữ dữ liệu cũ? | Hiển thị thông tin đã điền trước đó, cho phép sửa + matching lại | BA (HieuLuu) | 2026-05-15 | Answered |
| QA-007 | M | UC87 §2.3 | NĐT có nhận push notification khi có dự án mới được gán/matching? | Có | BA (HieuLuu) | 2026-05-15 | Answered |
| QA-008 | M | UC87 §2.3 | Sau khi đăng ký quan tâm, NĐT có thể hủy đăng ký không? | Có cho phép hủy | BA (HieuLuu) | 2026-05-15 | Answered |
| QA-009 | L | UC87 §1 | Cá nhân vs Tổ chức có khác biệt gì về form/danh sách? | Không — cùng field, cùng trải nghiệm | BA (HieuLuu) | 2026-05-15 | Answered |
| QA-010 | H | UC87 §2.2 | Thuật toán matching dựa trên tiêu chí nào? Trọng số ưu tiên? | Phương án Hybrid: bắt buộc khớp ít nhất 1 tiêu chí (Lĩnh vực HOẶC Địa bàn), các tiêu chí còn lại là bonus tăng thứ tự ưu tiên. Cân bằng giữa chính xác và đa dạng. | BA (HieuLuu) | 2026-05-15 | Answered |
| QA-011 | H | UC87 §2.2 | Matching score có hiển thị cho NĐT không? | Không hiển thị score — chỉ sắp xếp ngầm theo mức độ phù hợp | BA (HieuLuu) | 2026-05-15 | Answered |
| QA-012 | H | UC87 §2.3 | Khi NĐT sửa thông tin và matching lại, danh sách cũ bị thay thế hay merge? | Danh sách cũ bị thay thế hoàn toàn bằng kết quả matching mới | BA (HieuLuu) | 2026-05-15 | Answered |

---

## Open Questions

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| QA-013 | M | UC87 §2.3 | Dự án được admin gán thủ công có đánh dấu riêng (badge "Được gợi ý") để phân biệt với matching tự động không? | UX clarity — NĐT cần biết nguồn gốc gợi ý | Open |
| QA-014 | M | UC87 §2.3 | Nút "Hủy đăng ký quan tâm" hiển thị ở đâu? Trên Card danh sách hay chỉ trong Chi tiết? Có confirmation dialog không? | Tránh hủy nhầm — hành động không thể hoàn tác ngay | Open |
| QA-015 | M | UC87 §2.3 | Push notification khi có dự án mới — nội dung thông báo gồm gì? Tap notification → điều hướng đến đâu (Hub, Danh sách, hay Chi tiết dự án)? | Ảnh hưởng UX flow và thiết kế notification payload | Open |
| QA-016 | M | UC87 §2.2 | Matching realtime — nếu API matching timeout (>10s), hiển thị lỗi timeout hay cho phép NĐT chờ thêm? Có retry tự động không? | Matching có thể nặng hơn API thông thường — cần xác định UX khi chờ lâu | Open |
| QA-017 | L | UC87 §2.2 | Form bổ sung thông tin — có nút "Lưu nháp" để NĐT lưu tạm mà chưa matching không? Hay chỉ có "Xem dự án phù hợp"? | UX cho NĐT chưa sẵn sàng matching ngay | Open |
| QA-018 | L | UC87 §2.4 | Bảng hạng mục chi phí — có dòng "Tổng cộng" cuối bảng không? Tổng tự tính hay lấy từ API? | Đảm bảo consistency dữ liệu tài chính | Open |
| QA-019 | L | UC87 §2.1 | Phân quyền: Khách vãng lai (Guest) tap vào "Dự án kêu gọi đầu tư" trên Sidebar → redirect Đăng nhập hay ẩn menu item hoàn toàn? | Ảnh hưởng navigation design cho Guest | Open |

Priority: H = High (blocks design), M = Medium (affects scope), L = Low (nice to know)
Status: Open | Answered | Deferred
