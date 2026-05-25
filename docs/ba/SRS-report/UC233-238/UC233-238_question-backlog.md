# Question Backlog

> Generated: 2026-05-21
> Source files: UC233-238_BaoCaoTruocKhiThucHienDuAnDT_audited-v1.md

---

## Open Questions

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|

_(No open questions — all resolved.)_

Priority: H = High (blocks design), M = Medium (affects scope), L = Low (nice to know)
Status: Open | Answered | Deferred

---

## Answered Questions

| ID | Priority | Ref | Question | Answer | Answered By | Date | Status |
|----|----------|-----|----------|--------|-------------|------|--------|
| GAP-01 | M | UC233-238.1 Mục 1 | Thiếu bảng Mapping chi tiết UC → chức năng | Thông tin mapping đã được lưu tại Common Function (CF). Không cần bổ sung bảng riêng trong UC. | BA (quan.trinh) | 2026-05-21 | Answered |
| GAP-02 | L | UC233-238.1 Mục 2 (#1) | Placeholder Search bar không khớp phạm vi tìm kiếm | Đã sửa placeholder thành "Tìm kiếm theo mã báo cáo, tên dự án". Cập nhật tại UC v1.1. | BA (quan.trinh) | 2026-05-21 | Answered |
| GAP-03 | L | UC233-238.1 Mục 2 (#2) | Filter Năm thiếu tham chiếu CMR_16 | Đã bổ sung CMR_16 vào tham chiếu filter Năm. Cập nhật tại UC v1.1. | QC Agent | 2026-05-21 | Answered |
| GAP-04 | M | UC233-238.1 Mục 3 | Thiếu Empty State danh sách trống | Đã bổ sung: "Chưa có báo cáo nào. Nhấn 'Lập báo cáo' để tạo báo cáo mới." Cập nhật tại UC v1.1. | BA (quan.trinh) | 2026-05-21 | Answered |
| GAP-05 | L | UC233-238.1 Mục 3 | Thiếu vị trí nút [Lập báo cáo] | Đã bổ sung: Nút hiển thị trên header màn hình Danh sách (theo CS_02). Cập nhật tại UC v1.1. | QC Agent | 2026-05-21 | Answered |
| GAP-06 | H | UC233-238.2 Metadata | Phạm vi dự án = "Không có" vs trường Tên dự án (#001) | Đúng — báo cáo này KHÔNG chọn dự án từ dropdown. NĐT tự nhập tên dự án dự kiến (Textbox #001). Metadata "Phạm vi dự án = Không có" là chính xác. | BA (quan.trinh) | 2026-05-21 | Answered |
| GAP-07 | M | UC233-238.2 Mục 2 (#0) | Đơn vị tiếp nhận — nguồn dữ liệu dropdown | Nguồn dữ liệu: API danh mục đơn vị. Đã cập nhật tại UC v1.1. | BA (quan.trinh) | 2026-05-21 | Answered |
| GAP-08 | L | UC233-238.2 Mục 3 | CMR_18 Tab Navigation cho form đơn trang | CMR_18 tham chiếu theo chuẩn template, form single-page vẫn áp dụng (scroll navigation giữa các section). Giữ nguyên. | QC Agent | 2026-05-21 | Answered |
| GAP-09 | H | UC233-238.2 Mục 3 | API NĐT fail — mâu thuẫn CMR_12 | Khi API fail, các trường NĐT (#2-16) giữ Disabled + hiển thị trống. Không chuyển Enabled. Đây là ngoại lệ đã khai báo tại Mục 3: "Nếu thông tin sai → cần cập nhật tại nguồn." CMR_12 không áp dụng cho block NĐT này. | BA (quan.trinh) | 2026-05-21 | Answered |
| GAP-10 | H | UC233-238.2 Phần I | Nguồn API auto-fill NĐT — luồng thêm NĐT | Luồng: [+ Thêm NĐT] → chọn Loại NĐT (Radio) → hệ thống tự động gọi API fill thông tin dựa trên NĐT đã liên kết với dự án. Không có bước chọn NĐT từ dropdown riêng. | BA (quan.trinh) | 2026-05-21 | Answered |
| GAP-11 | M | UC233-238.2 Phần I (#17) | Vốn điều lệ — scope per NĐT hay chung | Mỗi NĐT Doanh nghiệp có 1 trường Vốn điều lệ riêng (#17 nằm trong Dynamic Block per NĐT). | BA (quan.trinh) | 2026-05-21 | Answered |
| GAP-12 | H | UC233-238.3 Action Mapping | Nhập từ file khi Chờ duyệt — logic ghi đè | Nhập từ file khi Chờ duyệt = GHI ĐÈ bản ghi hiện tại (CF_02). Hồ sơ chưa được tiếp nhận nên vẫn cho phép import lại. Không mâu thuẫn CMR_03 vì CMR_03 chỉ khóa chỉnh sửa thủ công, CF_02 import là luồng riêng. | BA (quan.trinh) | 2026-05-21 | Answered |
| GAP-13 | M | UC233-238.2 Mục 2 (#010a) | Tổng số lao động — 1 hay 3 trường | Cố định theo biểu mẫu gốc, không tách. Hiển thị gộp trên 1 dòng theo đúng mẫu A.III.3. | BA (quan.trinh) | 2026-05-21 | Answered |
| GAP-14 | L | UC233-238 toàn bộ | Thiếu Mapping UC chi tiết cho .2 và .3 | Thông tin mapping đã được lưu tại Common Function (CF). Giống GAP-01 — không cần bổ sung riêng. | BA (quan.trinh) | 2026-05-21 | Answered |
